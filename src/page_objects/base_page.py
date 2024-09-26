from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: webdriver.Remote, url: str):
        self.driver = driver
        self.url = url

    def open_url(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title

    def find_element(self, by, value):
        # wait for the element to be available before continuing
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((by, value))
        )

        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        # wait for the element to be available before continuing
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((by, value))
        )

        return self.driver.find_elements(by, value)
