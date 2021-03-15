import unittest
from commen.readfile import readfile
from cof.config import host_port
import os
from model_ui.login.loginController import LoginController
import ddt
import time


@ddt.ddt
class LoginCase(unittest.TestCase):
    purpath = os.path.join('./data/testdata.xlsx')
    data = readfile(purpath, 'login')

    @ddt.data(*data)
    @ddt.unpack
    def test_lo001_api_login(self, username, pwd):
        # pur = LoginController()
        # asserttext = pur.login(username, pwd)
        # self.assertIsNot(asserttext, host_port)
        pass

    def test_lo002_api_loginshot(self):
        pass

    purpath = os.path.join('./data/testdata.xlsx')
    data = readfile(purpath, 'login')

    @ddt.data(*data)
    @ddt.unpack
    def lo003_api_loginnext(self):
        pass

