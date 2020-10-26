from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo2:
    def setup(self):
        # self.driver = webdriver.Chrome("/Users/jiazhaopu/Downloads/chromedriver")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_demo2(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)
