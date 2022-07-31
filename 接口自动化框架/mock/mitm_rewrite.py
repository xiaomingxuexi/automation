
import json

from mitmproxy import http, ctx


class MitmRewrite:

    # 因为修改的内容是响应体的，所以使用response事件
    def response(self, flow: http.HTTPFlow):
        # 如果quote.json在url中
        if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
            # 将响应体转换成python对象
            data = json.loads(flow.response.content)
            # 修改第一条数据的name 为hogwarts000001
            data["data"]["items"][0]["quote"]["name"] = "hogwarts000001"
            # 将data转回json字符串，给response的text
            flow.response.text = json.dumps(data)
            # flow.response.json = data
            # ctx.log.info(f"print response{data}")
        else:
            ctx.log.info(flow.request.url)


# 将实例放入插件列表中
addons = [
    MitmRewrite()
]
