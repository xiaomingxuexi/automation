from configparser import ConfigParser
from common.constant_path import CONF_PATH
from common.constant_path import SWITCH_CONF_PATH,CONF_PATH_PER
from os import path

class MyConf(ConfigParser):
    def __init__(self):

        switch=ConfigParser()
        switch.read(SWITCH_CONF_PATH,encoding='utf8')
        env=switch.getint('env','env_version') #0,1,2,3

        super().__init__()

        if env == 0:
            self.read(path.join(CONF_PATH_PER,'conf.conf'))
        elif env==1:
            self.read(path.join(CONF_PATH_PER, 'conf1.conf'))
        elif env==2:
            self.read(path.join(CONF_PATH_PER, 'conf2.conf'))
        elif env==3:
            self.read(path.join(CONF_PATH_PER, 'conf3.conf'))


my_conf=MyConf()

if __name__ == '__main__':
    print(my_conf.get('logger','level'))