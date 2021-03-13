from model_ui.login.loginOperating import LoginOperating
from cof.config import host_port
import time
class LoginController(LoginOperating):
    def __init__(self):
        LoginOperating.__init__(self)
    def login(self,username,pwd):

        self.send_input_username(username)
        self.send_input_pwd(pwd)
        self.send_input_code()
        time.sleep(1)
        self.click_button_loginin()

        asstext=self.driver.current_url
        self.driver.get(host_port)

        return asstext