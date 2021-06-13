from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class RobotDriver():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--headless")
    driver_options.add_argument("--incognito")
    driver_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=driver_options)
    element_timeout = 10

    def get_element(self, element_locator) -> WebElement:
        return WebDriverWait(self.driver, self.element_timeout).until(presence_of_element_located(element_locator)
    )

    def get_driver(self):
        return self.driver

    def close_driver(self):
        return self.driver.quit()