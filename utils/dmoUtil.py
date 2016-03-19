#coding:utf-8

def blog_user_to_par(blog, user):
    return (blog.url,blog.title,blog.author_name,blog.time,blog.view,blog.comment,blog.like,blog.is_have_img,user.is_signed,user.focus,user.fans,user.blog_nums,user.word_nums,user.like_nums)
