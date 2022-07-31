"""
添加成员页面
"""
from selenium.webdriver.common.by import By
from wechat_web_test.page_object.base_page import BasePage
from wechat_web_test.page_object.contact_page import ContactPage


# 定义类的过程中，()里面代表子类的一个父类
class AddMemberPage(BasePage):
    # 定位是元祖形式，定位包含两个部分，定位方式和具体元素
    _username_locator = (By.ID, "username")
    _acctid_locator = (By.ID, "memberAdd_acctid")


    def goto_contact(self):
        """
        跳转通讯录页面
        :return:
        """

        return ContactPage(self.driver)

    def add_member(self, mem_name, mem_id, mem_phone):
        """添加成员操作
        """
        # 填写添加成员信息
        self.find(self._username_locator).send_keys(mem_name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(mem_id)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(mem_phone)
        # 点击保存
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def add_member_fail_by_name(self):
        """ name不填写，一个添加成员的反例操作。
        :return:
        """
        self.find(self._acctid_locator).send_keys("10000")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13188881111")
        # 点击保存
        # self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        error_list = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        # 寻找所有的错误信息，如果不为空，则返回
        error_message = [ele.text for ele in error_list if ele.text != ""]
        return error_message
