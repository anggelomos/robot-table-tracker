from selenium.webdriver.common.by import By
import time

class TicktickStatisticsPage():
    driver = None

    def __init__(self, driver):
        TicktickStatisticsPage.driver = driver
        self.driver = driver

        self.task_tab = driver.get_element((By.XPATH, "//div[@role='button' and contains(text(), 'Task')]"))
        self.focus_tab = driver.get_element((By.XPATH, "//div[@role='button' and contains(text(), 'Focus')]"))

    def load_focus_page(self):
        self.focused_time_label = self.driver.get_element((By.XPATH, "//p[contains(text(), 'Focused Duration')]//preceding-sibling::p"))

    def load_task_page(self):
        self.completion_rate_label = self.driver.get_element((By.XPATH, "//p[contains(text(), 'Completion Rate')]//preceding-sibling::p"))

    def go_to_focus(self):
        self.focus_tab.click()
        time.sleep(3)

    def get_focused_time(self) -> str:
        self.load_focus_page()
        return self.focused_time_label.text

    def go_to_task(self):
        self.task_tab.click()
        time.sleep(3)

    def get_completion_rate(self) -> str:
        self.load_task_page()
        return self.completion_rate_label.text

    