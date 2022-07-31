import logging
from common.conf_read import my_conf
from common.constant_path import LOG_PATH
level=my_conf.get('logger','level')
console_lever=my_conf.get('logger','console_lever')
file_lever=my_conf.get('logger','file_lever')



log_file=LOG_PATH

class MyLogger:
    def __new__(cls):
        # 日志收集器
        # 日志输出过滤器(输出到控制台,输出到文件)
        my_logger = logging.getLogger('my_logger')
        my_logger.setLevel(level)

        lsh = logging.StreamHandler()
        lsh.setLevel(console_lever)
        my_logger.addHandler(lsh)


        lfh=logging.FileHandler(log_file,mode='a',encoding='utf8')
        lfh.setLevel(file_lever)
        my_logger.addHandler(lfh)

        format='%(asctime)s - - Tread:%(threadName)s-->%(thread)d - - %(filename)s:%(lineno)d - - %(levelname)s----> %(message)s'
        lfh.setFormatter(logging.Formatter(format))
        lsh.setFormatter(logging.Formatter(format))


        return my_logger

my_logger = MyLogger()
if __name__ == '__main__':
    my_logger.debug('debug日志')
    my_logger.info('info日志')