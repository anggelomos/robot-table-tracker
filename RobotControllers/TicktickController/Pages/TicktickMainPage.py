from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TicktickMainPage():
    driver = None

    def __init__(self, driver):
        TicktickMainPage.driver = driver
        self.driver = driver

        self.base_element = driver.get_element((By.ID, "root"))
        self.user_bar = driver.get_element((By.XPATH, "//div[contains(@class, 't-user')]"))




