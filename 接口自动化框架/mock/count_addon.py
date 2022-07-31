

# 从mitmproxy 导入ctx
from mitmproxy import ctx
from mitmproxy import http


class Counter:
    def __init__(self):
        self.num = 0

    # 监听 request
    def request(self, flow):
        # num 的自增
        self.num = self.num + 1
        #log工具打印 We've seen ？ flows
        ctx.log.info("We've seen %d flows" % self.num)

class Counter2:
    def __init__(self):
        self.num = 0

    # 监听 request
    def request(self, flow):
        # num 的自增
        self.num = self.num + 2
        #log工具打印 We've seen ？ flows
        ctx.log.info("We've seen %d flows1" % self.num)


addons = [
    Counter(),Counter2()
]