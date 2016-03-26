#coding=utf-8
import jieba
from daoBase import dao

def title_word_top(blogs):
    words = []
    for blog in blogs:
        split_list = jieba.cut(blog.title)
        for word in split_list:
            words.append(word.encode('utf-8'))
    return cal_words(words)

def cal_words(words):
    word_list = {}
    for word in words:
        if len(word) <= 3:
            continue
        if word not in word_list.keys():
            word_list[word] = 1
        else:
            word_list[word] = word_list[word] + 1
    return sorted([(key,word_list[key]) for key in word_list.keys()], key=lambda t : t[1],reverse=True)





if __name__ == '__main__':
    l=title_word_top(dao.query_blog_by_time('2016-03-20 00:36:18','2016-03-26 20:36:18'))
    for a in l:

        print a[0], a[1]

