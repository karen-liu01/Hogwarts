# __author:liujinfang5
# data: 2020/10/28
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    base_url = ""
    def __init__(self, driver: WebDriver = None):
        # 如果没有传递过来driver,就创建,如果传递过来了,就用传递过来的driver
        if driver == None:
            options=Options()
            options.debugger_address="127.0.0.1:9222"
            self.driver=webdriver.Chrome(options=options)
        else:
            self.driver=driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # 如果继承的类没有赋予了url值,就使用子类的url值打开页面
        if self.base_url != "":
            self.driver.get(self.base_url)

    # 封装查找元素的方法
    def find(self, by, locator):
        return self.driver.find_element(by=by, value=locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by=by, value=locator)

