import unittest
from decimal import Decimal
from ddt import ddt,data
from common.do_excel import DOexcel
from common.my_log import my_logger
from common.request_tool import RequestTool,SessionTool
from common.constant_path import EXCEL_PATH
from common.do_sql import DoSQL
from common.conf_data import phone_number,password
from common.re_tool import re_replace





# 将充值用例设计全面,执行

@ddt()
class RechargeCase(unittest.TestCase):
    file = EXCEL_PATH
    sheet_name = 'Recharge'
    do_excel = DOexcel(file,sheet_name)
    cases= do_excel.read_obj()


    # 用例类加载之前会执行的方法
    @classmethod
    def setUpClass(cls) -> None:
        print('用例类开始加载')
        cls.do_sql=DoSQL()
        cls.request = SessionTool()

    # 用例类执行完，会执行的方法
    @classmethod
    def tearDownClass(cls) -> None:
        print('用例类执行完毕')
        cls.do_sql.close()
        cls.request.close()


    @data(*cases)
    def test_recharge(self,case):
        """先登录,再充值"""
        # 1.准备数据
        id = case.id
        description=case.description
        request_url=case.url
        request_method=case.method
        expectation=eval(case.expectation)
        sql_check=case.sql_check

        # re替换法(正则表达式)
        request_data=eval(re_replace(case.data))


        # replace替换法
        # case.data=case.data.replace('#phoneNumber#',phone_number)
        # case.data=case.data.replace('#password#',password)
        # request_data = eval(case.data)


        hold_money = request_data.get('holdMoney')


        # 获取充值余额
        print('充值余额')
        print(hold_money)
        print(type(hold_money))


        # 充值之前查询余额:
        if sql_check:
            sql_check=sql_check.replace('#phoneNumber#',phone_number)
            hold_money_last=self.do_sql.select_one(sql_check)[0]
            print('充值前余额')
            print(hold_money_last)
            print(type(hold_money_last))





        # 2.调用接口(日志,调接口)
        my_logger.info('调用接口开始')
        response=self.request.request(url=request_url,method=request_method,json=request_data)
        # my_logger.debug(request_url)
        # my_logger.debug(request_method)
        # my_logger.debug(request_data)
        # my_logger.debug(type(request_data))
        # my_logger.debug(response)
        # my_logger.debug(type(response))
        my_logger.info('调用接口结束')

        # 充值之后查询余额:
        if sql_check:
            hold_money_new = self.do_sql.select_one(sql_check)[0]
            print('充值后余额')
            print(hold_money_new)
            print(type(hold_money_new))


        # 3.比对结果
        try:
            self.assertEqual(expectation,eval(response))
            if sql_check:# Decimal转数据类型
                self.assertEqual(Decimal(hold_money),(hold_money_new-hold_money_last))
        except AssertionError as e:# 不通过
            print(description)
            print('预期',expectation)
            print('实际',response)
            print('不通过')
            try:
                self.do_excel.write(id+1,8,'不通过')
            except:
                my_logger.exception('Excel未关闭,结果回写失败')
            my_logger.info('用例',description,'执行不通过')
            my_logger.error(e)
            raise e

        else:# 通过
            print(description)
            print('通过')
            self.do_excel.write(id+1, 8, '通过')
            # my_logger.info('用例',description,'执行通过')


