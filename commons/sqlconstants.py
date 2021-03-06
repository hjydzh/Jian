#coding:utf-8

import Const

Const.SELECT_BLOG = """
SELECT
ID,TITLE,AUTHOR_NAME,`TIME`,VIEW_NUM,`COMMENT`,`LIKE`,IS_IMG
FROM HOT_BLOG
"""

Const.SELECT_VIEW = """
select BLOG_ID,VIEWS,AUTHOR_URL
from blog_view
"""

Const.INSERT_HOT_BLOG = """
insert into
hot_blog
(ID,TITLE,AUTHOR_NAME,`TIME`,SELECTED_TIME,VIEW_NUM,`COMMENT`,`LIKE`,IS_IMG,USER_IS_SIGNED,USER_FOUCS,USER_FANS,USER_BLOG_NUMS,USER_WORD_NUMS,USER_LIKE_NUMS)
values
(%s,%s,%s,%s,NOW(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

Const.GET_BLOG_SHOW_TIME_BY_URL = """
select show_time
from hot_blog
where id = '%s'
"""

Const.UPDATE_BLOG_SHOW_TIME_VIEW = """
update hot_blog
set show_time = %s ,last_view_num = %s, UPDATE_TIME=NOW()
where id = %s
"""

Const.QUERY_BLOG_BY_TIME = Const.SELECT_BLOG + """
WHERE SELECTED_TIME <='%s' and SELECTED_TIME >= '%s'
"""

Const.INSERT_VIEW = """
insert into blog_view
(BLOG_ID, VIEWS,AUTHOR_URL,CREATE_TIME)
values
(%s, %s,%s,NOW())
"""

Const.QUERY_HOUR_BLOGS = Const.SELECT_VIEW + """
WHERE HOURS_NUMS <=%s
"""

Const.QUERY_DAY_BLOGS = Const.SELECT_VIEW + """
WHERE  %s<=HOURS_NUMS and  DAYS_NUMS<=%s
"""

Const.UPDATE_BLOG_VIEWS = """
update blog_view
set
views = %s,
author_url = %s,
UPDATE_TIME = NOW()
where blog_id = %s

"""

Const.QUERY_VIEW_BLOG_ID = Const.SELECT_VIEW + """
where blog_id = '%s'
"""