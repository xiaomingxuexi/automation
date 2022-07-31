
import logging

import os

from interface.api_object.utils.file_tools import FileTool

# 初始化句柄
logger = logging.getLogger(__name__)
# 拼接日志文件所在的路径
file_path = os.sep.join([FileTool.get_interface_dir(), "logs"])

# 如果路径不存在 则创建

if not os.path.exists(file_path):
    os.mkdir(file_path)

# 拼接log文件和句柄

file_handle = logging.FileHandler(filename=file_path + "/apiobject.log", encoding="utf-8")

# 日志的输出格式

formatter = logging.Formatter(
    '[%(asctime).19s] %(process)d:%(levelname).1s %(filename)s:%(lineno)d:%(funcName)s: %(message)s]')

# 日志格式与句柄的绑定

file_handle.setFormatter(formatter)

# 控制台句柄定义

steam_handler = logging.StreamHandler()
# 日志格式与句柄的绑定
steam_handler.setFormatter(formatter)

# 与logger进行绑定

logger.addHandler(file_handle)
logger.addHandler(steam_handler)

# 设置展示/写入文件的日志的级别

logger.setLevel(logging.INFO)
