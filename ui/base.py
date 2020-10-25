from selenium import webdriver


class Base:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    def test_demo1(self):
        self.driver.get("http://www.baidu.com")




