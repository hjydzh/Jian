#coding:utf-8
from daoBase import insert
from daoBase import query
from commons.sqlconstants import *
from utils import dmoUtil

def insert_hot_blog(blog, user):
    par =dmoUtil.blog_user_to_par(blog,user)
    insert(Const.INSERT_HOT_BLOG,[par])

def get_blog_show_time_by_url(url):
    obj = query(Const.GET_BLOG_SHOW_TIME_BY_URL % url)
    if not obj:
        return None
    return obj[0][0]

def update_blog_show_time(url, show_time):
    par = (show_time,url)
    insert(Const.UPDATE_BLOG_SHOW_TIME,[par])