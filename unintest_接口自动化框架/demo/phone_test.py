# 随机生成手机号
"""
构造手机号
# 1.有效号段--------->随机拿一个有效号段(188)
# 2.补齐------------->在有效号段之后补充8位
"""


# 1.自己定义一个列表,存储有效号段,就需要知道有效号段到底有哪些.
# 2.网络接口,运营商,通信部..........
# 3.找开发,有效号段的验证,"本身接口肯定是要判断手机号合不合法的"--->开发说:177不合法,产品也说177不合法,177不用考虑
# ----------->找开发给我们开放一个校验手机号的接口(前缀接口)----->有效前缀
# import random

# per_phone_list = [134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,178,147]
# print(len(per_phone_list)) # 19个,生成一个0-18之间的随机数,从列表中就能获取一个有效号段了！

# 随机获取有效号段
# while True:
#     rand = random.randint(0, 18)
#     print(per_phone_list[rand])

# 在有效号段之后拼接8位:--------->每一位都是0~9之间的某数字！
# for i in range(8):
#     item=random.randint(0,9)
#     str_item=str(item)


# 生成随机手机号:
# rand = random.randint(0, 18)
# phone=str(per_phone_list[rand])
#
# for i in range(8):
#     item=random.randint(0,9)
#     str_item=str(item)
#     phone+=str_item
#
# print(phone)

# 生成一个联通手机号
# 生成一个移动手机号
# 生成一个电信手机号
import random

def phone_number():
    """随机生成手机号"""
    per_phone_list = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 178, 147]
    rand = random.randint(0, 18)
    phone = str(per_phone_list[rand])

    for i in range(8):
        item = random.randint(0, 9)
        str_item = str(item)
        phone += str_item
    return phone

if __name__ == '__main__':
    print(phone_number())