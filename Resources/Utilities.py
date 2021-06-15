import calendar
from datetime import date

class Utilities():

    @classmethod
    def get_current_date_data(cls):
        current_date = date.today()
        week_of_month = cls._get_week_of_the_month(current_date.year, current_date.month, current_date.day)

        return {
            "month": date.today().strftime("%b"),
            "week_of_month": week_of_month,
            "weekday": date.today().strftime("%a"),
            "date": current_date.strftime("%Y-%m-%d")
        }

    @classmethod
    def _get_week_of_the_month(cls, year, month, day) -> int:
        year = int(year)
        month = int(month)
        day = int(day)

        for week_number, week in enumerate(calendar.monthcalendar(year, month)):
            if day in week:
                return week_number+1

