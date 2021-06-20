from RobotControllers.TicktickController.Pages.TicktickMainPage import TicktickMainPage
from selenium.webdriver.common.by import By


class TicktickHabitsPage:
    driver = None

    def __init__(self, driver):
        TicktickHabitsPage.driver = driver
        self.driver = driver
        self.dynamic_habit_checked = driver.get_element((By.XPATH, "//div[not(contains(@class, 'preview'))]/*[contains(text(), '{0}')]//following-sibling::div//div[contains(@class,'progressBar')]//div[contains(@class, 'today')]//*[contains(@class, 'habit_list_complete')]"), dynamic_element=True)

