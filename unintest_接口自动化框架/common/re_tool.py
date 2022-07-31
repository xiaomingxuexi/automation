import re
from common.conf_data import my_conf

def re_replace(data):
    while re.search('#(.+?)#',data):
        result=re.search('#(.+?)#', data)
        option = result.group(1)
        value = my_conf.get('user', option)
        data = data.replace(result.group(), value)
    return data

if __name__ == '__main__':
    data = '{"accountPWD":"#password#","phoneNumber":"#phoneNumber#"}'
    data=re_replace(data)
    print(data)