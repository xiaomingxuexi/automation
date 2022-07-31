import unittest
from cases import test_login
from MyHTMLTestRunner import HTMLTestRunner
from common.constant_path import REPORT_PATH,CASE_PATH
report_file=REPORT_PATH


suite=unittest.TestSuite()
loader=unittest.TestLoader()

# suite.addTests(loader.loadTestsFromModule(test_login))
suite.addTests(loader.discover(CASE_PATH))

with open(report_file,mode='wb') as fw:
    runner=HTMLTestRunner( stream=fw,title='第一次接口测试',description='登陆报告',tester='tester')
    runner.run(suite)

