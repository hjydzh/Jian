#coding:utf-8

class BlogView:

    def __init__(self):
        self.blog_id = None
        self.views = None
        self.hour_views = []
        self.day_views = []
        self.hours_num = 0
        self.days_num = 0
        self.author_url=''

