#coding:utf-8
from daoBase import insert
from commons.sqlconstants import *
from utils import dmoUtil

def insert_hot_blog(blog, user):
    par =dmoUtil.blog_user_to_par(blog,user)
    insert(Const.INSERT_HOT_BLOG,[par])