from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from ui.podemo1.page.addmemer_page import AddMemberPage
from ui.podemo1.page.base_page import BasePage


class MainPage(BasePage):

    # def __init__(self):
    #     options = Options()
    #     options.debugger_address("127.0.0.1:9222")
    #     self.driver = webdriver.Chrome(options=options)


    def goto_addmember(self):
        self.driver.find_element(By.XPATH,"//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div/span[2]")
        return AddMemberPage(self.driver)