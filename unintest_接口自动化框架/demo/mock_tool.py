"""
后端先行
并行开发
后端接口没写好,前端页面已经要用了

mock------------>模拟http请求和响应

自动化测试代码,接口还没好;

"""

from unittest.mock import Mock

# 模拟登陆成功
request_login_true=Mock(return_value='{"status_code":"200","message":"登陆成功"}')

# response=request_tool.request('url,method,headers,data')

response=request_login_true('url,method,headers,data')
print(response)

# 模拟机号格式不对
request_login_phone_error=Mock(return_value='{"status_code":"20001","message":"手机号格式不对"}')


response=request_login_phone_error('url,method,headers,data')

print(response)