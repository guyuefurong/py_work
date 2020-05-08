"""
@Author  : Laura
@File    : write_zt_config.py
@Time    : 2020/4/9 16:50
"""

import configparser
# 获取配置文件
cf=configparser.ConfigParser()
cf.read("case.config", encoding="utf-8")

# 读取配置文件数据
host = cf.get("MYSQL", "db_host")
port = cf.getint("MYSQL", "db_port")
user = cf.get("MYSQL", "db_user")
password = cf.get("MYSQL", "db_password")
database = cf.get("MYSQL", "db_database")

print(host+str(port),user,database)

