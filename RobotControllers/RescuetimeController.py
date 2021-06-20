from Resources.Utilities import Utilities
from RobotControllers.BaseController import BaseController

import os
import requests
from datetime import date

class RescuetimeController(BaseController):

    API_key = os.getenv("RT_API_KEY")
    current_date = date.today().strftime("%Y-%m-%d")
    hours_endpoint = f"https://www.rescuetime.com/anapi/data?key={API_key}&perspective=interval&restrict_kind=productivity&interval=hour&restrict_begin={current_date}&restrict_end={current_date}&format=json"

    def get_hours(self, current_date, hour_type):
        retrieved_hours = 0
        hours_request = requests.get(RescuetimeController.hours_endpoint).json()

        if hour_type == "productive":
            hour_code = [1, 2]
        elif hour_type == "neutral":
            hour_code = [0]
        elif hour_type == "distracted":
            hour_code = [-1, -2]
        else:
            raise ValueError("hour_type is not 'productive', 'neutral' or 'distracted'")

        for hour_type in hours_request["rows"]:
            if hour_type[-1] in hour_code:
                retrieved_hours += hour_type[1]

        retrieved_hours = Utilities().round_number(retrieved_hours/3600)

        return current_date, retrieved_hours
