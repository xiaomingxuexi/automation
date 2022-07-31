"""
什么是正则:
    正则不是python的一部分;
    re模块,支持正则

    正则表达式用来处理字符串;

    按照一定的规则,匹配字符串;



"""

import re
from common.conf_read import my_conf
# search()
# 自行了解:---->match(),findall,sub()\

# re.search('正则规则','字符串')


# 在字符串中按照正则规则查找内容,并返回,匹配不到则返回None

# s='\n12\n34 hello 5678 python 999 ... 000'

# print(re.search('.',s))# .代表任意字符
#
# print(re.search('....',s))# 拿连续的4个任意字符,遇到换行符不匹配
#
# print(re.search('\.\.\.',s))# 拿到.本身

# 字符集
# s1='1234 hello 5678 python 999999 ... 000'

# print(re.search('[abcde]',s1))# 按顺序存在abcde中的其中一个都返回
#
# print(re.search('[on]',s1))# 存在abcde中的其中一个都返回
# 其他写法
# print(re.search('[\a-k]',s1))# a到k

# 预定义字符集
# print(re.search('\d',s1))# \d 匹配数字
# print(re.search('\d\d\d\d\d\d',s1))# \d 匹配数字

# 数量词
# print(re.search('9\d',s1)) #9后面带数字
# print(re.search('9\d*',s1)) #9后面带数字的全部


# print(re.search('\d+',s1))#数字后面带数字的全部
# print(re.search('9\d+',s1))#9后面带数字的全部

# print(re.search('\d?',s1))#数字后面的一个数字
# print(re.search('9\d?',s1))#9后面带一个数字的一个数字

# print(re.search('\d{2}',s1))# 找2次\d
# print(re.search('\d{4}',s1))# 找4次\d
# print(re.search('\d{6}',s1))# 找6次\d
# print(re.search('\d{5,7}',s1))# 找5到7次\d 默认先找7次的

# 贪婪模式,往多了取----------->数量词之后加一个 ?  关闭贪婪模式
# print(re.search('\d*?',s1)) # 取0次
# print(re.search('\d+?',s1)) # 取1次
# print(re.search('9\d+?',s1))#9后面带数字取1次
# print(re.search('\d{5,7}?',s1))# 找5到7次\d 取5次的


# 边界匹配
# ^ 开头
# $ 结尾

# s2='hello python hello java'
# print(re.search('^hello',s2))# 匹配hello开头的
# print(re.search('^python',s2))# 匹配python开头的

# print(re.search('java$',s2))# 匹配java结尾的
# print(re.search('python$',s2))# 匹配python结尾的

# re的分组
"""

s3='#python#,#java#,#html#,#css#,#js#,#sql#,#linux#'

# result=re.search('#.+#',s3) #拿第一个#号到最后一个
# print(result)
# result=re.search('#.+?#',s3) #拿第一个#号到第一个#号
# print(result)

# result=re.search('#.+?#,#.+?#,#.+?#,#.+?#,#.+?#',s3) #拿多个#xxx#
# print(result)
#
# # 分组
# result=re.search('#(.+?)#,#(.+?)#,#(.+?)#,(#.+?#)(,#.+?#)',s3) #拿多个#xxx#
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.group(4))
# print(result.group(5))



"""

data = '{"accountPWD":"#password#","phoneNumber":"#phoneNumber#"}'
#     #phoneNumber# ------------>  phoneNumber(具体的手机号)
"""
# 第一次替换
result=re.search('#(.+?)#',data)

print(result)
print(result.group())# #password#

print(result.group(1))# password

password=my_conf.get('user',result.group(1))
print(password)

data=data.replace(result.group(),password)
print(data)

# {"accountPWD":"123456","phoneNumber":"#phoneNumber#"}

# 第二次替换
result=re.search('#(.+?)#',data)

print(result.group())# #phoneNumber#
print(result.group(1))# phoneNumber

phone=my_conf.get('user',result.group(1))
print(phone)

data=data.replace(result.group(),phone)
print(data)

# {"accountPWD":"123456","phoneNumber":"18700000025"}

# 第三次替换
result=re.search('#(.+?)#',data)
print(result)
# None
"""

# 循环处理
def re_replace(data):
    while re.search('#(.+?)#',data):
        result=re.search('#(.+?)#', data)
        replace_option=result.group(1)
        value=my_conf.get('user', replace_option)
        data = data.replace(result.group(), value)
    return data

new_data=re_replace(data)
print(new_data)