from wechat.podemo.page.main_page import MainPage
# from faker import Faker,factory
import random

class TestWx:
    def setup(self):
        self.main=MainPage()

    def testdown(self):
        self.main.driver.quit()

    def test_add_member_success(self):
        username="zhangsan"
        account="222"
        phoneno="18800009911"
        addmember=self.main.goto_add_members()
        addmember.add_member_success(username, account, phoneno)
        assert username in addmember.get_member()

    # def test_add_member(self):
    #     username ="lisi"
    #     account = "22222"
    #     phoneno = "18800009912"
    #     addmember = self.main.goto_add_members()
    #     addmember.add_member()
    #     addmember.add_member_success(username,account,phoneno)