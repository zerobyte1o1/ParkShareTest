from model_ui.login.loginElement import LoginElement


class LoginOperating(LoginElement):
    def __init__(self):
        LoginElement.__init__(self)

    def send_input_username(self, username):
        self.get_input_username().send_keys(username)

    def send_input_pwd(self, pwd):
        self.get_input_pwd().send_keys(pwd)

    def send_input_code(self, code='0000'):
        self.get_input_code().send_keys(code)

    def click_button_loginin(self):
        self.get_button_loginin().click()
