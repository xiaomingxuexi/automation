
# 首页
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from apptest.podemo1.base.base_page import BasePage
from apptest.podemo1.page.addresslist_page import AddressListPage


class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_addresslist(self):
        # click [通讯录]
        self.find_and_click(*self.addresslist_element)
        return AddressListPage(self.driver)
