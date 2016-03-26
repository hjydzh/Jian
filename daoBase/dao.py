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

def update_blog_show_time_view(url, show_time, view):
    par = (show_time, view,url)
    insert(Const.UPDATE_BLOG_SHOW_TIME_VIEW,[par])

def query_blog_by_time(start_time, end_time):
    obj = query(Const.QUERY_BLOG_BY_TIME % (end_time, start_time))
    if not obj:
        return None
    return dmoUtil.results_to_blogs(obj)

def insert_view(blog_view):
    par = (blog_view.blog_id, blog_view.views, blog_view.hour_views, blog_view.day_views,blog_view.author_url)
    insert(Const.INSERT_VIEW,[par])


def query_hour_blogs(hours):
    obj = query(Const.QUERY_HOUR_BLOGS % hours)
    if not obj:
        return None
    return dmoUtil.results_to_blogs(obj)

def query_day_blogs(hours, days):
    obj = query(Const.QUERY_DAY_BLOGS % (hours,days))
    if not obj:
        return None
    return dmoUtil.results_to_blogs(obj)

def update_blog_views(blog_views):
    pars = [dmoUtil.view_to_par(view) for view in blog_views]
    insert(Const.UPDATE_BLOG_VIEWS,pars)

if __name__ == '__main__':
    a = query_hour_blogs(12)
    print a