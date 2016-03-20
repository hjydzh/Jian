#coding=utf-8
import MySQLdb
from commons.CommonConst import *

def insert(sql, parms):
    try:
        conn=MySQLdb.connect(host=Const.HOST_IP,user=Const.USER_NAME,passwd=Const.PASSWD,db=Const.DB,charset="utf8")
        cursor = conn.cursor()
        for parm in parms:
            n = cursor.execute(sql, parm)
        conn.commit()
        cursor.close()
    except :
        return
    finally:
        conn.close()


def query(sql):
        try:
            conn=MySQLdb.connect(host=Const.HOST_IP,user=Const.USER_NAME,passwd=Const.PASSWD,db=Const.DB,charset="utf8")
            cursor = conn.cursor()
            cursor.execute(sql)
            obj = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print e
            return None
        finally:
            if conn is not None:
                conn.close()
        return obj