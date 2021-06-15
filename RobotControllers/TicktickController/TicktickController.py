from Resources.TestData import TestData
from RobotControllers.BaseController import BaseController
from RobotControllers.TicktickController.Pages.TicktickHabitsPage import TicktickHabitsPage
from RobotControllers.TicktickController.Pages.TicktickLoginPage import TicktickLoginPage
from RobotControllers.TicktickController.Pages.TicktickStatisticsPage import TicktickStatisticsPage

import re


class TicktickController(BaseController):


    def go_to_main_page(self):
        self.robot_driver.get_driver().get(TestData.ticktick_signin_url)

    def login(self):
        self.go_to_main_page()
        login_page = TicktickLoginPage(self.robot_driver)

        login_page.enter_email(TestData.ticktick_email)
        login_page.enter_password(TestData.ticktick_password)
        login_page.sign_in()

    def go_to_statistics(self):
        self.robot_driver.get_driver().get(TestData.ticktick_statistics_url)

    def go_to_habits(self):
        self.robot_driver.get_driver().get(TestData.ticktick_habits_url)

    def get_focused_time(self):
        self.go_to_statistics()

        statistics_page = TicktickStatisticsPage(self.robot_driver)
        statistics_page.go_to_focus()
        raw_focused_hours = statistics_page.get_focused_time()

        extracted_hours = re.findall("\d+", raw_focused_hours)
        focused_hours = float(extracted_hours[0])
        focused_minutes = float(extracted_hours[1])
        focused_time = round(focused_hours + focused_minutes/60, 2)

        return focused_time

    def get_task_completion_percentage(self):
        self.go_to_statistics()

        statistics_page = TicktickStatisticsPage(self.robot_driver)
        statistics_page.go_to_task()
        raw_completion_rate = statistics_page.get_completion_rate()

        completion_rate = int(re.match("\d+", raw_completion_rate).group(0))

        return completion_rate

    def get_habits(self) -> dict:
        habits = {}
        self.go_to_habits()

        habits_page = TicktickHabitsPage(self.robot_driver)

        for habit in TestData.ticktick_habit_list:
            habit_is_checked = self.robot_driver.is_element_present(habits_page.dynamic_habit_checked, habit)
            if habit_is_checked:
                habits[habit] = "|"
            else:
                habits[habit] = "-"

        return habits