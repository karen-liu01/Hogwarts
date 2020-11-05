# __author:liujinfang5
# data: 2020/10/28
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
        locator=(By.CSS_SELECTOR, '.ww_checkbox')
        self.wait_until_click(locator)
        return True

    # 获取联系人的列表[包括页面元素很多的时候]
    def get_member(self):
        # 查看页面是否有分页的元素出现
        pages: str=self.finds(By.CSS_SELECTOR, '.ww_pageNav_info_text')
        print(pages)
        # if len(pages) == 0:
        # 如果列表为0,证明只有第一页,所有的名字都在第一页;
        # 无论是否只有一页,都需要获取第一页的数据
        members_name_list=self.finds(By.XPATH, '//*[@id="member_list"]/tr/td[2]')
        # 将第一页找到的元素的title都放到title_list中
        title_list = []
        # title_list=[element.get_attribute("title") for element in members_name_list]
        for element in members_name_list:
            # 获取title
            title_list.append(element.get_attribute("title"))
        if len(pages) > 0:
            # 证明有翻页功能,需要去翻页
            page: str=self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            num, total=page.split('/')
            print(int(num), int(total))
            n=int(num)
            t=int(total)
            for i in range(1, t+1):
                self.find(By.CSS_SELECTOR, '.ww_commonImg_PageNavArrowRightNormal').click()
                members_name_list=self.finds(By.XPATH, '//*[@id="member_list"]/tr/td[2]')
                # title_list=[element.get_attribute("title") for element in members_name_list]
                for element in members_name_list:
                    # 获取title
                    title_list.append(element.get_attribute("title"))
        return title_list
