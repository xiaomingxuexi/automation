
from mitmproxy import ctx

num = 0


# 监听 request
def request(flow):
    global num
    # num 的自增
    num +=1
    # log工具打印 We've seen ？ flows
    ctx.log.info("We've seen %s flows" % num)
