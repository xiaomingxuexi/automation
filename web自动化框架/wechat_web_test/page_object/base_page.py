"""
封装所有页面对象共性的操作，比如driver 的实例化
"""
import time

import yaml
from selenium import webdriver


class BasePage:

    _base_url = None
    # 当子类没有构造函数的时候，在实例化的过程中，会自动父类的构造函数
    # 所以，每个PO 在实例化过程中，都会执行构造函数的逻辑
    # 问题： 如何避免driver 的重复实例化
    def __init__(self, base_driver=None):
        """
        告诉父类的构造函数，如果传参了，不需要进行重复的实例化操作
        如果没有传参， 那么就是第一次的实例化操作，需要进行实例化
        :param base_driver:
        """
        # 如果base_driver 为真， 为真就是不等于None，那么就不需要重复实例化的操作
        if base_driver:
        # 非第一次实例化操作
        # 为了保证，后面的子类在使用的过程中，都具有driver属性，所以需要做赋值操作
            self.driver = base_driver
        # 如果base_driver 为None/假， 那么就需要对Driver进行实例化
        else:
            # 第一次实例化
            # 没加self 是局部变量
            self.driver = webdriver.Chrome()
            #  Unable to locate element: 碰到这个报错，在元素定位没有问题的场景下
            # 就是太快了，加隐式等待
            self.driver.implicitly_wait(3)
            # 1. 访问企业微信主页面
            if self._base_url != None:
                self.driver.get(self._base_url)
            # 2. 定义cookie，cookie信息从已经写入的cookie文件中获取
                cookie = yaml.safe_load(open("../data/cookie.yaml"))
            # 3. 植入cookie
                for c in cookie:
                    self.driver.add_cookie(c)
                time.sleep(3)
                # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
                self.driver.get(self._base_url)
            else:
                # 如果url 为空，那么抛出异常
                pass

    def find(self, by, locaotr=None):
        """
        点击操作， 需要兼容两种情况
        :return:
        """
        # 如果传入一个参数，证明是元祖
        if locaotr == None:
            # xxx((1, 2)) -> xxx(*(1,2))->xxx(1,2)
            # 如果传入元祖，则做解包操作
            res = self.driver.find_element(*by)
        # 如果传入两个参数，证明是分开传递的
        else:
            res = self.driver.find_element(by, locaotr)
        print(f"找到的元素为{res}")
        return res

    def finds(self):
        pass

