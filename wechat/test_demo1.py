import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_getcookies(self):
        # # 打开想要复用的页面，获取cookies
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 注意一定是cookies方法，不是cookie方法
        # cookies = self.driver.get_cookies()
        # print(cookies)
        cookies = [
            {'domain': '.work.weixin.qq.com', 'expiry': 1603755481, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': True, 'value': '1vn1fd6'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853968680858'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853968680858'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': True,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1918277658, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': True, 'value': 'f341ca2e8f6643b0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': True,
             'value': '0-qCYYS9agE7RWBwlH6wmoCobg45eSXbj1JS2YvUv6tyJZJYjjVpgHIOGhlbe2r2cKl1sdppJZAI1-lrqMu7ZvyNzaSEBXclJf8SgTYp4K7bw6MqpORNqZ57xM9WKWqoAlwT754tUW9dgjbnqNctr1N5X37DtU7whWIMTR_afVyQM_va1up1B9ErLd6TPjybRSEi5yyFlyvjW7Gt0EIPjQur70yBj1z6d0snXO2tRgqtET3u4X-eOiOYmkSyGMPXWDRZOWI5S5DsEt4QNuVdeA'},
            {'domain': '.qq.com', 'expiry': 1666796190, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1713181936.1596639546'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
             'value': 'aa58296817e88d37e7d09e2177848c25efc7ba0a2888733cef5502aa194c7079'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
             'value': 'vW7UUpljae'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635145540, 'httpOnly': False,
                                      'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True,
                                      'value': '1603607009'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606316325, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324987168209'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': True,
             'value': 'LVxBbNjqZXL2l5_9tLWJRxKPV6PiT8As5SFD6C0ZTSUJjBlprUoJEr3uKydFXe86'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': True, 'value': '3380508672'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True,
             'value': '7479486553145375'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': True, 'value': '5417295000'},
            {'domain': '.qq.com', 'expiry': 1603810590, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1717047806.1603723962'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603755481, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '1vn1fd6'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': True,
             'value': 'a2821459'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1628175543, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'}]
        # 打开想要复用的页面，获取cookies
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # cookies 一定要加引号
        db = shelve.open("cookies")
        db['cookie'] = cookies
        db.close()
        self.driver.refresh()

    # 导入联系人并验证界面
    def test_wx(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        # 点击导入通讯录按钮_上传文件
        # self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item_title:nth-child(2)').click()
        self.driver.find_element(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        sleep(2)
        file = "/Users/jiazhaopu/QGjobs/Hogwarts/wechat/通讯录批量导入模板.xlsx"
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys(file)
        sleep(2)
        # 获取文件名称并断言
        filename = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert "通讯录批量导入模板.xlsx" == filename