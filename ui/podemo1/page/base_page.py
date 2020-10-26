# 基类
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

# 隐式等待的问题：web页面的加载有dom结构，当页面加载速度慢的时候，导致有些元素出现了，但是仍然无法找到，可能是因为这些元素的
# 某些属性没有加载完成，这种情况下，需要使用显示等待
# 显示等待
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""
    def __init__(self,driver:WebDriver=None):
        if driver == None:
            options = Options()
            options.debugger_address("127.0.0.1:9222")
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver = driver
        # 隐式等待
        self.driver.implicitly_wait(5)
        # 显示等待
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable())

        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self,by,locator):
        self.driver.find_element(by,locator)

    def finds(self, by, locator):
        self.driver.find_elements(by, locator)

