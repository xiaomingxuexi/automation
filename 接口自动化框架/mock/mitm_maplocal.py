

from mitmproxy import http


class MitmMapLocal:

    # 因为是maplocal 所以使用request事件
    def request(self, flow: http.HTTPFlow):
        # 如果quote.json在url中
        if "quote.json" in flow.request.pretty_url:
            # 打开本地的quote.json来使用
            with open("quote.json", encoding="utf-8") as f:
                # 创造响应体，注意  如果使用的mitm不是7版本的  此处是http.HTTPResponse
                # make的第一个参数是响应码，第二个是响应体，第三个是头信息
                flow.response = http.Response.make(
                    200,
                    f.read(),
                    {"Content-Type": "application/json"}
                )

# 将实例放入插件列表中
addons = [
    MitmMapLocal()
]
