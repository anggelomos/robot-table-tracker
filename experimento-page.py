from selenium.webdriver.common.by import By

class ExperimetPage(object):

    driver = None

    def __init__(self, driver):
        ExperimetPage.driver = driver
        self.driver = driver
        
    elemento_1 = driver.find_element(By.XPATH, '//button[text()="Some text"]')
    elemento_2 = driver.find_elements(By.XPATH, '//button')

    
    @classmethod
    def funcion_pagina(cls):
        cls.elemento_1.click()
        cls.elemento_2.sendKeys("Hola")
