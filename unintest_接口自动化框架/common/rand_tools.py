import random

def rand_phone_number():
    """随机生成手机号"""
    per_phone_list = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 178, 147]
    rand = random.randint(0, 18)
    phone = str(per_phone_list[rand])

    for i in range(8):
        item = random.randint(0, 9)
        str_item = str(item)
        phone += str_item
    return phone

def rand_account():
    """随机生成用户名"""
    '''
    有一个前缀,写死,(不去定义列表，存储多个前缀,随机获取一个)
    拼接数字,拼接8次随机数字0-9
    '''
    account='colatest'
    for i in range(8):
        item = random.randint(0, 9)
        str_item = str(item)
        account += str_item
    return account



if __name__ == '__main__':
    phone=rand_phone_number()
    account=rand_account()
    print(phone)
    print(account)
    data='{"accountId":"123456abcd","accountName":"大力士","accountPWD":"123456","phoneNumber":"18700000000","accountType":"1"}'
    # data_new=data.replace('替换谁','替换成什么')
    # data是原来的字符串
    # data_new就是替换之后的新字符串
    data=data.replace('123456abcd',account)
    # print(data)

    data = data.replace('18700000000', phone)
    print(data)