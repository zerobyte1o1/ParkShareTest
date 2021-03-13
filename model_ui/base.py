from selenium.webdriver.support.select import Select
import time
from lib.driverfactory import DriverFactory

class Base():
    def __init__(self,flag=0):
        self.driver=DriverFactory.get_driver('chrome',flag)

    def get_select_option(self,select,index):
        s1=Select(select)
        s1.select_by_index(index)
