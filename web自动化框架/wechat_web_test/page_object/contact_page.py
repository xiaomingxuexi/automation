from selenium.webdriver.common.by import By

from wechat_web_test.page_object.base_page import BasePage


class ContactPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    #def __init__(self, base_driver):
     #每个页面都有一个相同的构造函数，不优雅，而且不好维护

    def goto_add_member(self):
        # 如果出现A->B， B->A循环导入的场景，那么需要把其中一个的导包
        # 放到方法里面解决此问题。
        from wechat_web_test.page_object.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def get_list(self):
        eles = self.driver.find_elements(By.CSS_SELECTOR,
                                  ".member_colRight_memberTable_td:nth-child(2)")
        #[Web]
        name_list = [web_ele.text for web_ele in eles]
        # for web_ele in eles:
        #     name_list.append(web_ele.text)
        return name_list
