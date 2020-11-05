# __author:liujinfang5
# data: 2020/10/28
from time import sleep

from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from wechat.podemo.page.add_member_page import AddMemberPage
from wechat.podemo.page.base_page import BasePage


class MainPage(BasePage):
    # 主页面的链接:https://work.weixin.qq.com/wework_admin/frame   使用浏览器复用
    # self.driver.get("https://work.weixin.qq.com/wework_admin/frame ")
    base_url="https://work.weixin.qq.com/wework_admin/frame"

    # 在主页面只封装点击添加成员跳转到添加成员界面,第一个方法,点击页面下方的添加成员
    def goto_add_members(self):
        # 点击添加联系人按钮
        # self.driver.find_element(By.XPATH, '//*[@class="index_service_cnt js_service_list"]/a[1]/div[1]').click()
        # self.find(By.XPATH, '//*[@class="index_service_cnt js_service_list"]/a[1]/div[1]').click()
        # 显示等待逻辑  返回的元素指定了类型，才可以调用click方法
        locator=(By.XPATH, '//*[@class="index_service_cnt js_service_list"]/a[1]/div[1]')
        # element:WebElement = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        element=self.wait_until_click(locator)
        element.click()
        # 跳回页面必须加括号
        return AddMemberPage(self.driver)

    # 第二个方法:点击页面顶部的tab通讯录
    def goto_member_from_tab(self):
        # 点击通讯录
        self.find(By.ID, "menu_contacts").click()
        # 点击添加联系人,第二种方法等待页面可点击后再点击
        # self.find(By.XPATH, '//*[@id="js_contacts39"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        # locator=(By.XPATH, '//*[@id="js_contacts39"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]')
        locator=(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)")

        # 自己定义一个显示等待函数，实现等页面跳转后进行下一步操作
        def wait_for_next(x: WebDriver):
            try:
                # 将传进来的locator解包，因为locator中有两个元素
                x.find_element(*locator).click()
                # 等能定位到输入框输入姓名元素后再允许点击
                return x.find_element(By.ID, "username")
            except:
                return False

        # x不需要传值，会将webdriver传递进去
        WebDriverWait(self.driver, 20).until(wait_for_next)

        return AddMemberPage(self.driver)
