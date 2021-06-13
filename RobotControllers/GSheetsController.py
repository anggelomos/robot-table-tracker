import sys

from Resources.TestData import TestData
from RobotControllers.BaseController import BaseController

import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

class GSheetsController(BaseController):

    def __init__(self):

        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        creds = None
        if os.path.exists(TestData.google_token_path):
            creds = Credentials.from_authorized_user_file(TestData.google_token_path, SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    TestData.google_credential_path, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(TestData.google_token_path, 'w') as token:
                token.write(creds.to_json())

        self.service = build('sheets', 'v4', credentials=creds)

    def read_board_tracker_data(self, range:str) -> list:
        sheet = self.service.spreadsheets()

        board_tracker_data = sheet.values() \
                                    .get(spreadsheetId=TestData.id_sheet_board_tracker, range=range) \
                                    .execute().get('values')

        if board_tracker_data is None:
            board_tracker_data = [["None"]]

        return board_tracker_data

    def upload_board_tracker_data(self, data_board_tracker):
        sheet = self.service.spreadsheets()

        sheet_last_date = self.read_board_tracker_data(TestData.range_current_date)

        if sheet_last_date[0][0] not in data_board_tracker:
            self.insert_blank("ROWS", start_index=1, end_index=2)

        sheet.values()\
                .update(
                        spreadsheetId=TestData.id_sheet_board_tracker,
                        range=TestData.range_write_board_data,
                        valueInputOption="USER_ENTERED",
                        body=TestData.get_body_request_update_sheet([data_board_tracker]))\
                .execute()



    def insert_blank(self, dimension_type, start_index, end_index):
        sheet = self.service.spreadsheets()

        sheet.batchUpdate(
                spreadsheetId=TestData.id_sheet_board_tracker,
                body=TestData.get_body_request_insert_blank(
                                                            dimension_type,
                                                            start_index,
                                                            end_index
                                                            ))\
                                .execute()

g_cont = GSheetsController()
g_cont.upload_board_tracker_data(['2021-06-13', 2.58, 1.25, 50])


