from time import sleep
from selenium.webdriver.common.by import By
from wechat.podemo.page.base_page import BasePage


class AddMemberPage(BasePage):
    def add_member_success(self, username, account, phoneno):
        # 查找页面上的元素,姓名电话账号,然后提交
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phoneno)
        self.find(By.NAME, "sendInvite").click()
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        # sleep(2)
        # 等到复选框出现，证明添加元素成功
        locator = (By.CSS_SELECTOR, '.ww_checkbox')
        ele = self.wait_until_click(locator)
        return True

    # 在通讯录页面点击添加成员进行添加
    def add_member(self):
        self.find(By.CSS_SELECTOR, '.js_add_member').click()
        sleep(2)

    # 获取联系人的列表
    def get_member(self):
        # 获取分页的数据
        while True:
            members_name_list=self.finds(By.XPATH, '//*[@id="member_list"]/tr/td[2]')
            title_list = []
            for element in members_name_list:
                # 获取title
                title_list.append(element.get_attribute("title"))
            self.find()

        return title_list
