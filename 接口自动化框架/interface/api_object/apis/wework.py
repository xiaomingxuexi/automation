
from interface.api_object.apis.base_api import BaseApi


class WeWork(BaseApi):

    def get_access_token(self, corpid, corpsecret):
        '''
        获取access_token
        :return:
        '''
        # 定义凭证
        # corpid = "ww75abb8519b57cec6"
        # corpsecret = "vvavK-3lew1LhtP2sLdfkieOEe8CJy5hJpdJ2ceKiEI"

        # 从接口调用的时候传入 获取token的参数
        corpid = corpid
        corpsecret = corpsecret

        url = "/gettoken"

        # 定义请求参数
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

        # 发 get 请求
        r = self.send("GET", url, params=params)
        # 打印响应
        print(r.json())

        access_token = r.json()['access_token']
        self.access_token = access_token
