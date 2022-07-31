
import uuid

import jsonpath
import requests

from interface.api_object.utils.log_util import logger


class BaseApi:
    BaseUrl = "https://qyapi.weixin.qq.com/cgi-bin/"

    def send(self, method, url, **kwargs):
        '''
        发起请求，使用那个工具去发起可被替换
        :return:
        '''
        # 调用requests工具发起接口请求
        url = self.BaseUrl + url
        logger.info(f"接口请求操作，请求的url为：{url}")
        logger.info(f"接口请求操作，请求的参数为：{kwargs}")
        logger.info(f"接口请求操作，请求的params为：{kwargs.get('params')}")
        res = requests.request(method=method, url=url, **kwargs)
        logger.info(f"接口请求后，返回的参数为：{res.text}")
        return res

    def my_jsonpath(self, json_boj, exp):
        return jsonpath.jsonpath(json_boj, exp)

    def get_union_id(self):
        return str(uuid.uuid4()).split("-")[0]
