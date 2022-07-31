from common.conf_read import my_conf

# 能登陆成功的手机号和密码
phone_number=my_conf.get('user','phoneNumber')
password=my_conf.get('user','password')
