from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:

    def __init__(self,driver:WebDriver):
        self.driver = driver




    def register_success(self):
        self.driver.find_element(By.ID,"corp_name").send_keys("aaa")
        self.driver.find_element(By.ID,"manager_name").send_keys("bbbb")
        return True

    def register_fail(self):
        self.driver.find_element(By.ID,"corp_name").send_keys("aaa")
        self.driver.find_element(By.ID,"manager_name").send_keys("bbbb")
        return True