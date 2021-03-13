from model_ui.base import Base

class LoginElement(Base):
    def __init__(self):
        # 传值

        # 第二个参数是flag，用于判断是否是login操作，默认是0
        Base.__init__(self)


    def get_input_username(self):
        return self.driver.find_element_by_id('uname')
    def get_input_pwd(self):
        return self.driver.find_element_by_id('upass')
    def get_input_code(self):
        return self.driver.find_element_by_id('imgcode')
    def get_button_loginin(self):
        return self.driver.find_element_by_id("button")
