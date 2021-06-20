from RobotControllers.TicktickController.Pages.TicktickMainPage import TicktickMainPage
from selenium.webdriver.common.by import By


class TicktickLoginPage:

    driver = None

    def __init__(self, driver):
        TicktickLoginPage.driver = driver
        self.driver = driver
        self.email_input = driver.get_element((By.ID, "emailOrPhone"))
        self.password_input = driver.get_element((By.ID, "password"))
        self.signin_button = driver.get_element(
            (By.XPATH, "//button[contains(text(), 'Sign In')]")
        )

    def enter_email(self, ticktick_email):
        self.email_input.send_keys(ticktick_email)

    def enter_password(self, ticktick_password):
        self.password_input.send_keys(ticktick_password)

    def sign_in(self):
        self.signin_button.click()
        TicktickMainPage(self.driver)
