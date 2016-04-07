#coding:utf-8
from dmo.Blog import Blog
from dmo.BlogView import BlogView

def blog_user_to_par(blog, user):
    return (blog.url,blog.title,blog.author_name,blog.time,blog.view,blog.comment,blog.like,blog.is_have_img,user.is_signed,user.focus,user.fans,user.blog_nums,user.word_nums,user.like_nums)

def results_to_blogs(results):
    return [ result_to_blog(result) for result in results]

def result_to_blog(result):
    blog = Blog()
    blog.url = result[0]
    blog.title = result[1]
    blog.author_name = result[2]
    blog.time = result[3]
    blog.view = result[4]
    blog.comment = result[5]
    blog.like = result[6]
    blog.is_have_img = result[7]
    return blog

def results_to_views(results):
    return [ result_to_view(result) for result in results]

def result_to_view(result):
    blog_view = BlogView()
    blog_view.blog_id = result[0].encode('utf-8')
    blog_view.views = result[1].encode('utf-8')
    blog_view.author_url = result[2].encode('utf-8')
    return blog_view

def view_to_par(view):
    return (view.views, view.author_url, view.blog_id)