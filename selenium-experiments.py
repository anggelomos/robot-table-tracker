from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver_options = webdriver.ChromeOptions()
driver_options.add_argument("--incognito")
driver_options.add_argument("--start-maximized")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=driver_options)

driver.get("http://www.python.org")
assert "Python" in driver.title