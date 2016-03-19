#coding:utf-8

import Const

Const.INSERT_HOT_BLOG = """
insert into
hot_blog
(ID,TITLE,AUTHOR_NAME,`TIME`,SELECTED_TIME,VIEW_NUM,`COMMENT`,`LIKE`,IS_IMG,USER_IS_SIGNED,USER_FOUCS,USER_FANS,USER_BLOG_NUMS,USER_WORD_NUMS,USER_LIKE_NUMS)
values
(%s,%s,%s,%s,NOW(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""