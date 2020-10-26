from selenium.webdriver.remote.webdriver import WebDriver


class AddMemberPage:

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def add_member(self):
        username = "aaa"
        account = "bbbb"

        return True