#coding:utf-8
import sys
sys.path.append('/home/workspace/Jian')
from daoBase import dao
from utils import HttpUtil
from BeautifulSoup import BeautifulSoup
from service import service
import json
import time
from utils.QueueThread import QueueThread


def update_hour_view():
    views = dao.query_hour_blogs(25)
    thread_views = QueueThread(update_view_hours, 4, views)
    thread_views.run()
    dao.update_blog_views(thread_views.result)


def update_day_view():
    views = dao.query_day_blogs(25, 10)
    thread_views = QueueThread(update_view_days, 4, views)
    thread_views.run()
    dao.update_blog_views(thread_views.result)

def update_view_days(view):
    blog = query_view_by_url(view.author_url, view.blog_id)
    view.day_views = append_view_time(view.day_views, blog.view)
    view.days_num = 1 + view.days_num
    return view

def update_view_hours(view):
    blog = query_view_by_url(view.author_url, view.blog_id)
    view.hour_views = append_view_time(view.hour_views, blog.view)
    view.hours_num = 1 + view.hours_num
    return view


def append_view_time(view_str, view_nums):
    views = json.loads(view_str)
    views.append({time.time() : view_nums})
    return json.dumps(views)

def query_view_by_url(author_url, blog_url):
    url = 'http://www.jianshu.com/' + author_url
    soup = BeautifulSoup(HttpUtil.request(url))
    blogs_soup = soup.find(attrs={"class": "article-list latest-notes"}).findAll('li')
    for blog_soup in blogs_soup:
        blog = service.parse_blog(blog_soup)
        if blog.url == blog_url:
            return blog



if __name__ == '__main__':
    update_hour_view()

