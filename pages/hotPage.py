#coding:utf-8
import sys
sys.path.append('/home/workspace/Jian')
from daoBase import dao
import time
import userPage
from utils import redisUtil
import json
from dmo.BlogView import BlogView
from service import service

def visit(exec_time, former_blogs):
    try:
        blogs = service.find_blogs('http://www.jianshu.com/')
        redis = redisUtil.connect()
        blog_urls = []
        for blog in blogs:
            if ('简书' or '简叔') in blog.title:
                continue
            blog_urls.append(blog.url)
            user = userPage.user_info(blog.author_url)
            show_time = dao.get_blog_show_time_by_url(blog.url)
            if not show_time:
                pass
                dao.insert_hot_blog(blog,user)
            else:
                interval = int(time.time() - exec_time)
                dao.update_blog_show_time_view(blog.url, show_time + interval, blog.view)
            service.view_time_insert(time.time(), blog.view, blog.url, redis)
        for blog in former_blogs:
            if ('简书' or '简叔') in blog.title:
                continue
            if blog.url not in blog_urls:
                views = service.get_blog_view(blog.url, redis)
                redis.delete( "blog:" + blog.url.split('/')[2])
                blog_view = BlogView()
                blog_view.blog_id = blog.url
                blog_view.author_url = blog.author_url
                blog_view.views = json.dumps(views)
                dao.insert_view(blog_view)
    except Exception as e:
        print e
        return []
    return blogs




if __name__ == '__main__':
    exec_time = time.time()
    former_blogs = []
    while True:
        former_blogs =visit(exec_time, former_blogs)
        print('休息5分钟')
        exec_time = time.time()
        time.sleep(60 * 5)
