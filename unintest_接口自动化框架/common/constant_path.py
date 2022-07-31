import os
from os import path


# 构造前面相对路径
# print(__file__)
# print(path.dirname(__file__))
# print(path.dirname(path.dirname(__file__)))

# 构造后面死路径

# datas\test_login.xlsx
# logs\log.out
# reports\report.html

path_excel=R'datas/test_login.xlsx'
path_log=R'logs/log.out'
path_report=R'reports/report.html'
path_conf=R'confs/conf.conf'
path_recharge=R'cases'
path_switch=R'confs/switch.conf'
path_confs='confs/'

path_before=path.dirname(path.dirname(__file__))

# print(path.join(path_before+'/',path_excel))
# # print(path.join(path_before+'/',path_log))
# # print(path.join(path_before+'/',path_report))
EXCEL_PATH=path.join(path_before+'/',path_excel)
LOG_PATH=path.join(path_before+'/',path_log)
REPORT_PATH=path.join(path_before+'/',path_report)
CONF_PATH=path.join(path_before+'/',path_conf)
CASE_PATH=path.join(path_before+'/',path_recharge)
SWITCH_CONF_PATH=path.join(path_before+'/',path_switch)
CONF_PATH_PER=path.join(path_before+'/',path_confs)