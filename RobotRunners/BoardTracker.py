from Resources.TestData import TestData
from Resources.Utilities import Utilities
from RobotControllers.TicktickController.TicktickController import TicktickController
from RobotControllers.RescuetimeController import RescuetimeController
from RobotControllers.GSheetsController import GSheetsController
from assertpy import assert_that

rescuetime_controller = RescuetimeController()
ticktick_controller = TicktickController()
gsheets_controller = GSheetsController()


def runner_board_tracker():
    current_date_data = Utilities().get_current_date_data()
    current_date, productive_hours = rescuetime_controller.get_hours(current_date_data["date"], hour_type="productive")
    ticktick_controller.login()
    focused_hours = ticktick_controller.get_focused_time()
    amount_of_pomos = ticktick_controller.get_amount_of_pomos()
    task_completion_percentage = ticktick_controller.get_task_completion_percentage()
    habits = ticktick_controller.get_habits()

    date_data_as_list = [str(value) for value in current_date_data.values()]
    productive_stats = [
        str(amount_of_pomos),
        str(productive_hours),
        str(focused_hours),
        str(task_completion_percentage)
    ]
    habits_as_list = [value for value in habits.values()]

    data_board_tracker = date_data_as_list + productive_stats + habits_as_list
    gsheets_controller.upload_board_tracker_data(data_board_tracker)

    retrieved_data_board_tracker = gsheets_controller.read_board_tracker_data(TestData.range_write_board_data)[0]

    assert_that(retrieved_data_board_tracker).is_equal_to(data_board_tracker)
    ticktick_controller.robot_driver.close_driver()

    print(f"\n{current_date=}\n{amount_of_pomos=}\n{productive_hours=}\n{focused_hours=}\n{task_completion_percentage=}\n")

if __name__ == "__main__":
    runner_board_tracker()
