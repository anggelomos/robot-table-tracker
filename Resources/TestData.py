import os
import sys
import re
import base64

class TestData():

    project_name = "robot-board-tracker"
    project_base_path = [path for path in sys.path if re.search(r"robot-table-tracker$", path)][0]

    ticktick_signin_url = "https://ticktick.com/signin"
    ticktick_statistics_url = "https://ticktick.com/webapp/#statistics"
    ticktick_email = "anggelomos@outlook.com"
    ticktick_password = base64.b64decode(os.getenv("TK_PASS")).decode("utf-8")

    google_credential_path = project_base_path + "\\Resources\\board-tracker_274683942061-8mij18mtpvr6tklhbblbfcie94cad7j7.apps.googleusercontent.com.json"
    google_token_path = project_base_path + "\\Resources\\board-tracker-token.json"
    id_sheet_board_tracker = "1dq9nlVUsBtW4y7nVL2h-QJdjD8-Fyhj0lUHbekIZEhY"
    range_current_date = "Sheet1!A2:A2"
    range_write_board_data = "Sheet1!A2:D2"

    @classmethod
    def get_body_request_update_sheet(cls,values, major_dimension:str = "ROWS") -> dict:
        body_request = {
                        "majorDimension": major_dimension,
                        "values": values
                    }

        return body_request

    @classmethod
    def get_body_request_insert_blank(cls, dimension, start_index, end_index) -> dict:
        body_request = {
            "requests": [
                {
                    'insertDimension': {
                        'range': {
                            'dimension': dimension,
                            'startIndex': start_index,
                            'endIndex': end_index
                        }
                    }
                }
            ]
        }

        return body_request

