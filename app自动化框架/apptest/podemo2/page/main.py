from selenium.webdriver.common.by import By

from apptest.podemo2.base.base_page import BasePage
from apptest.podemo2.page.market import Market


class Main(BasePage):

    def goto_market(self):
        self.find_and_click(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/post_status"]')
        self.find_and_click(By.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='行情']")
        return Market(self.driver)
