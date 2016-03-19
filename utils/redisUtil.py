#coding:utf-8

from commons.CommonConst import *
import redis

def connect():
    s =  redis.Redis(host=Const.HOST_IP,password=Const.REDIS_PASSWD)
    s.lpush('a', 'sss')

redis = connect()
