from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from ui.podemo.register_page import RegisterPage


class LoginPage:

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        # 点击登录
        self.driver.find_element(By.XPATH, "//*[@id='wework_admin.loginpage_wx_$']/main/div[2]/a")
        # return 到logoinpage
        return RegisterPage(self.driver)