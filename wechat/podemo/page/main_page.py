# data: 2020/10/28
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from wechat.podemo.page.add_member_page import AddMemberPage
from wechat.podemo.page.base_page import BasePage


class MainPage(BasePage):

    # 在主页面只封装点击添加成员跳转到添加成员界面
    # 主页面的链接:https://work.weixin.qq.com/wework_admin/frame   使用浏览器复用
    def goto_add_members(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame ")
        self.base_url = "https://work.weixin.qq.com/wework_admin/frame"

        # 点击添加联系人按钮
        # self.driver.find_element(By.XPATH, '//*[@class="index_service_cnt js_service_list"]/a[1]/div[1]').click()
        self.find(By.XPATH, '//*[@class="index_service_cnt js_service_list"]/a[1]/div[1]').click()

        # 跳回页面必须加括号
        return AddMemberPage(self.driver)