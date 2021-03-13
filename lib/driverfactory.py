# 单例模式:为了解决测试用例执行的时候打开多个浏览器的问题
from selenium import webdriver
from cof.config import host_port, Account
import time


class DriverFactory:
    # 静态属性
    driver = None

    @classmethod
    def get_driver(cls, browser, flag):
        # 静态属性可以通过类名的方式来调用，判断如果driver为None,则还没有打开浏览器，
        if DriverFactory.driver == None:
            if browser == "chrome":
                DriverFactory.driver = webdriver.Chrome()


            DriverFactory.driver.maximize_window()
            DriverFactory.driver.get(host_port)
            DriverFactory.driver.implicitly_wait(10)

            # 抢租客登陆
            if flag == 1:
                DriverFactory.login(Account.gettenantname(), Account.gettenantpwd())
            # 出租方登陆
            elif flag == 2:
                DriverFactory.login(Account.getlandlordname(), Account.getlandlordpwd())
            # 物业登陆
            elif flag == 3:
                DriverFactory.login(Account.getpropertyname(), Account.getpropertypwd())
            # 平台登陆
            elif flag == 4:
                DriverFactory.login(Account.getplatformname(), Account.getplatformpwd())

        return DriverFactory.driver

    # 用户登录
    @classmethod
    def login(cls, username, password, checkcode='0000'):
        # 打开登录首页
        DriverFactory.driver.get(host_port)
        # 输入用户名
        DriverFactory.driver.find_element_by_id('uname').send_keys(username)
        # 输入密码
        DriverFactory.driver.find_element_by_id('upass').send_keys(password)
        # 输入验证码
        code = DriverFactory.driver.find_element_by_id('imgcode')
        code.clear()
        code.send_keys(checkcode)
        # 点击登录按钮
        DriverFactory.driver.find_element_by_id('button').click()


if __name__ == '__main__':
    DriverFactory.get_driver('chrome')
