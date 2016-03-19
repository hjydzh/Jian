#coding:utf-8

from BeautifulSoup import BeautifulSoup
from dmo.Blog import Blog
from utils import DateUtil
from utils import HttpUtil
from commons.TimeConst import *
import re
from daoBase import dao
import time
import userPage

def visit():
    try:
        blogs = __search()
        for blog in blogs:
            if '简书' in blog.title:
                continue
            user = userPage.user_info(blog.author_url)
            print(blog.title)
            dao.insert_hot_blog(blog,user)
    except:
        pass


def __search():
    url = 'http://www.jianshu.com/'
    soup = BeautifulSoup(HttpUtil.request(url))
    blogs = map(lambda blog_soup:__parse(blog_soup), soup.find(attrs={"class": "article-list thumbnails"}).findAll('li'))
    return blogs

def __parse(blog_soup):
    blog = Blog()
    try:
        a =  blog_soup['class']
        blog.is_have_img = 1
    except KeyError:
        pass
    p = blog_soup.find(attrs={"class": "list-top"})
    blog.author_name = p.find('a').text.encode('utf-8')
    blog.author_url = p.find('a')['href'].encode('utf-8')
    blog.time = DateUtil.str_to_time(p.find('span')['data-shared-at'], Const.JIAN_STYLE,)
    title_wrap = blog_soup.find(attrs={"class": "title"}).find('a')
    blog.title = title_wrap.text.encode('utf-8')
    blog.url = title_wrap['href'].encode('utf-8')
    nums_str = blog_soup.find(attrs={"class": "list-footer"}).text.encode('utf-8')
    pattern = re.compile(r'阅读 ([0-9]+)· 评论 ([0-9]+)· 喜欢 ([0-9]+)')
    nums = pattern.search(nums_str).groups()
    blog.comment = nums[1]
    blog.view = nums[0]
    blog.like = nums[2]
    return blog

if __name__ == '__main__':
    while True:
        visit()
        print('休息5分钟')
        time.sleep(60 * 5)