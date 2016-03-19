#coding:utf-8
import Const
from utils.PasswdUtil import get_passwd_dict

#普通常量类
Const.PASSWD_FILE = '/home/passwd.txt'

PASSWD_DICT = get_passwd_dict()



Const.WEIBO_USERNAME = PASSWD_DICT['weibo_username']

Const.WEIBO_PASSWD = PASSWD_DICT['weibo_passwd']

Const.HOST_IP = PASSWD_DICT['host_ip']

Const.USER_NAME = PASSWD_DICT['usr_name']

Const.PASSWD = PASSWD_DICT['password']

Const.DB = PASSWD_DICT['db']

Const.REDIS_PASSWD = PASSWD_DICT['redis_passwd']




