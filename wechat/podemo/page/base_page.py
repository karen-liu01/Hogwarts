# __author:liujinfang5
# data: 2020/10/28
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        # 如果没有传递过来driver,就创建,如果传递过来了,就用传递过来的driver
        if driver == None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver = driver
        self.driver.maximize_window()
        # 三种等待方式：强制等待 sleep 弊端：每次都强等，效率低
        # 隐士等待(每次调用find方法都会出发隐式等待)  弊端：只能判断元素是否出现，无法判断是否可操作或者点击
        # 显式等待 加载页面的时候有时候元素出现了，但是元素依然找不到，可能是因为元素的属性没有加载完成，可以等到元素可操作了，再去操作元素
        # 当报错  元素未附着到dom中时，可使用显示等待webdriverwait
        self.driver.implicitly_wait(5)
        # 如果继承的类没有赋予了url值,就使用子类的url值打开页面
        if self.base_url != "":
            self.driver.get(self.base_url)

    # 封装查找元素的方法
    def find(self, by, locator):
        return self.driver.find_element(by=by, value=locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by=by, value=locator)

    # 显示等待的封装
    def wait_until_click(self, locator, timeout=10):
        element: WebElement = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        return element
