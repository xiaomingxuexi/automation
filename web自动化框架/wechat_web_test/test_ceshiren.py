import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestCeshiren:
    def setup_class(self):
        browser = os.getenv("env")
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        else:
            self.driver = webdriver.Chrome()

        self.driver.get("https://ceshiren.com")
        self.driver.implicitly_wait(10)

    def test_search(self):
        self.driver.find_element(By.ID, 'search-button').click()
        self.driver.find_element(By.ID, 'search-term').send_keys("python 21" + Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, '[title=打开高级搜索]').click()

    def teardown_class(self):
        self.driver.quit()
