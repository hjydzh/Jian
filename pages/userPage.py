#coding:utf-8

from dmo.User import User
from utils import HttpUtil
from BeautifulSoup import BeautifulSoup

def user_info(user_url):
    url = 'http://www.jianshu.com' + user_url
    soup = BeautifulSoup(HttpUtil.request(url))
    user = User()
    base_info_soup = soup.find(attrs={"class": "basic-info"})
    user.name = base_info_soup.find('h3').text.encode('utf-8')
    signed_soup = base_info_soup.find(attrs={"class": "signed_author"})
    if signed_soup:
        user.is_signed = 0
    nums_soup = soup.find(attrs={"class": "user-stats"}).findAll('b')
    user.focus = int(nums_soup[0].text.encode('utf-8'))
    user.fans = int(nums_soup[1].text.encode('utf-8'))
    user.blog_nums = int(nums_soup[2].text.encode('utf-8'))
    user.word_nums = int(nums_soup[3].text.encode('utf-8'))
    user.like_nums = int(nums_soup[4].text.encode('utf-8'))
    return user

if __name__ == '__main__':
    user_info('/users/b6f444a41f75')


