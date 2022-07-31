import unittest
from ddt import ddt,data
from common.do_excel import DOexcel
from common.my_log import my_logger
from common.request_tool import RequestTool
from common.constant_path import EXCEL_PATH
from common.do_sql import DoSQL
from common.rand_tools import rand_phone_number,rand_account



# 将登陆用例设计全面,执行

@ddt()
class LoginTest(unittest.TestCase):
    file = EXCEL_PATH
    sheet_name = 'Login'
    do_excel = DOexcel(file,sheet_name)
    data_s= do_excel.read_obj()
    request=RequestTool()

    # 用例执行之前会执行的方法
    def setUp(self) -> None:
        print('用例开始执行')

    # 用例执行之后会执行的方法
    def tearDown(self) -> None:
        print('用例执行完毕')

    # 用例类加载之前会执行的方法
    @classmethod
    def setUpClass(cls) -> None:
        print('用例类开始加载')
        cls.do_sql=DoSQL()

    # 用例类执行完，会执行的方法
    @classmethod
    def tearDownClass(cls) -> None:
        print('用例类执行完毕')
        cls.do_sql.close()



    @data(*data_s)
    def test_login(self,d):
        # 1.准备数据
        id = d.id
        description=d.description
        request_url=d.url
        request_data=eval(d.data)
        request_method=d.method
        expectation=eval(d.expectation)



        # 2.调用接口(日志,调接口)
        my_logger.info('执行'+description+'用例,调用登陆接口,登陆手机号为:'+request_data.get('phoneNumber'))
        response=self.request.request(url=request_url,method=request_method,json=request_data)
        # my_logger.debug(request_url)
        # my_logger.debug(request_method)
        # my_logger.debug(request_data)
        # my_logger.debug(type(request_data))
        # my_logger.debug(response)
        # my_logger.debug(type(response))
        my_logger.info('调用' + description + '接口结束' + '响应结果为:' + str(response))

        # 3.比对结果
        try:
            self.assertEqual(expectation,eval(response))
        except AssertionError as e:# 不通过
            print(description)
            print('预期',expectation)
            print('实际',response)
            print('用例'+description+'不通过')
            self.do_excel.write(id+1,8,'不通过')
            my_logger.info('执行'+description+'用例,结果为不通过')
            my_logger.exception(e)
            raise e

        else:# 通过
            print(description)
            print('通过')
            my_logger.info('执行' + description + '用例,结果为通过')
            self.do_excel.write(id+1, 8, '通过')
            # my_logger.info('用例',description,'执行通过')


# 将注册用例设计全面,执行

@ddt()
class RegisterCase(unittest.TestCase):
    # 创建Excel对象
    file = EXCEL_PATH
    sheet_name = 'Register'
    # 读取Excel,返回结果是列表嵌套对象
    do_excel = DOexcel(file,sheet_name)
    cases= do_excel.read_obj()
    # 创建request对象
    request=RequestTool()
    do_sql=DoSQL()


    @data(*cases)
    def test_register(self,case):# 创建测试用例方法，(方法需要以test开头)
        # 1.准备数据(接口参数,预期结果)
        row=case.id+1
        url=case.url
        method=case.method
        # data=eval(case.data)
        expectation=eval(case.expectation)
        description=case.description
        # sql_check=case.sql_check #sql,None

        # 去数据库中查询,直到生成的手机号不存在,使用该手机号
        per_sql='select * from cola_member where phoneNumber="'
        while True:
            phone = rand_phone_number()
            sql=per_sql+phone+'"'

            count=self.do_sql.select_count(sql)
            if count==0:
                break


            # select count()-------->0才用这个phone

            # 数据替换
        account = rand_account()
        case.data=case.data.replace('*phone_number*',phone)
        case.data=case.data.replace('*account*',account)
        if case.sql_check:
            case.sql_check=case.sql_check.replace('*phone_number*',phone)
        if case.sql_recover:
            case.sql_recover = case.sql_recover.replace('*phone_number*', phone)





        # 2.调用接口
        my_logger.info('执行'+description+'用例,调用注册接口,手机号为:'+str(eval(case.data).get('phoneNumber')))
        response=self.request.request(url=url,method=method,data=eval(case.data))
        # 调用接口之后,数据库会新增一条数据,18700000000
        my_logger.info('调用'+description+'接口结束'+'响应结果为:'+str(response))
        # 3.比对结果
        try:
            self.assertEqual(expectation,eval(response))
            # 也要去做数据库校验;
            # 又select count()--->为1,表示断言成功,注册成功
            if case.sql_check:
                self.assertEqual(1,self.do_sql.select_count(sql=case.sql_check))
            if case.sql_recover:
                self.do_sql.delete(sql=case.sql_recover)
        except AssertionError as e:
            print('用例:'+description+'不通过')
            print(case.data)
            my_logger.info('执行'+description+'用例,结果为不通过')
            my_logger.exception(e)
            self.do_excel.write(row,8,'不通过')
            raise e
        else:
            print('用例:' + description + '通过')
            my_logger.info('执行'+description+'用例,结果为通过')
            self.do_excel.write(row, 8, '通过')


