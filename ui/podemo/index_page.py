from selenium import webdriver
from selenium.webdriver.common.by import By

from ui.podemo.login_page import LoginPage
from ui.podemo.register_page import RegisterPage


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome("/Users/jiazhaopu/Downloads/chromedriver")
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        # 点击登录
        self.driver.find_element(By.XPATH,"//*[@id='indexTop']/div[2]/aside/a[1]")
        # return 到logoinpage
        return LoginPage(self.driver)

    def goto_register(self):
        # 点击登录
        self.driver.find_element(By.XPATH, "//*[@id='tmp']/div[1]/a")
        # return 到logoinpage
        return RegisterPage(self.driver)
