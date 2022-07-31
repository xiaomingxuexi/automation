"""
使用Pytest 做测试用例的框架
添加成员的测试用例类
"""
from wechat_web_test.page_object.main_page import MainPage


class TestAddMember:



    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        """
        添加成员测试
        # 1. 在首页，点击添加成员
        # 2. 在添加成员页面， 填写成员信息，点击保存
        # 3. 返回通讯录页面，查看数据是否保存成功
        :return:
        """
        # 参数: 手工用例中的测试数据，实参，具体传入的数据，在用例层
        # 测试用例（测试数据）和 页面对象要实现分层
        # 页面对象需要哪一些数据，需要表述出来。
        # 使用pytest 参数化优化
        name, accid, phone = "提莫7", "131", "13100001115"
        # 通过return 实例对象，可以直接方法.方法的方式，实现链式调用
        res = self.main.goto_add_member().\
                add_member(name,accid, phone).\
                get_list()
        # 与手工测试一致，断言刚刚添加的成员是否在结果中，如果在获取的结果中
        # 证明用例通过，反之用例失败
        assert name in res

    def test_add_member_fail(self):
        # 错误信息列表
        error_list = self.main.goto_add_member().\
            add_member_fail_by_name()
        assert "请填写姓名" in error_list

    def teardown(self):
        self.main.driver.quit()
