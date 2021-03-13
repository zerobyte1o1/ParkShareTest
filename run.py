import unittest
import time
from cof.config import scope
from commen.HTMLTestRunner import HTMLTestRunner


report_title='test1'
report_desc="this is my frist test program"
report_path="./report"
path=report_path+f'/test{time.strftime("%Y%m%d%H%M%S")}.html'
with open(path,'wb') as report:

    suite=unittest.defaultTestLoader.discover(start_dir='test_case',pattern=f'test_{scope}*.py')
    runner=HTMLTestRunner(stream=report,title=report_title,description=report_desc)
    runner.run(suite)