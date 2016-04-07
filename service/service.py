#coding:utf-8

from utils import DateUtil
from BeautifulSoup import BeautifulSoup
from utils import HttpUtil
from dmo.Blog import Blog
import re
from commons.TimeConst import *

def view_time_insert(timestamp, view, blog_url, redis):
    blog_id = blog_url.split('/')[2]
    redis.zadd('blog:' + blog_id, timestamp, view)
    redis.expire('blog:' + blog_id, 86400)

def get_blog_view(blog_url, redis):
    views = redis.zrangebyscore('blog:'+blog_url.split('/')[2], 0 ,100000,withscores=True)
    return [{float(view[0]):view[1]} for view in views]

def catch(func):
    def _catch(*args, **kwargs):
        try:
            f = func(*args, **kwargs)
            return f
        except Exception as e:
            print(e)
            pass
    return _catch


def find_blogs(url):
    soup = BeautifulSoup(HttpUtil.request(url))
    blogs = map(lambda blog_soup:parse_blog(blog_soup), soup.find(attrs={"class": "article-list thumbnails"}).findAll('li'))
    return filter(lambda blog : blog is not None, blogs)


@catch
def parse_blog(blog_soup):
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
    blog.comment = int(nums[1])
    blog.view = int(nums[0])
    blog.like = int(nums[2])
    return blog

