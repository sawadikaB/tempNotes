# coding:utf-8
import sys
from goose import Goose
from goose.text import StopWordsChinese
reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://news.sina.com.cn/o/2017-09-27/doc-ifymkxmh7444203.shtml'
urllist = ['http://world.chinadaily.com.cn/2017-09/29/content_32635418.htm']
g = Goose({
        'stopwords_class': StopWordsChinese,
        'browser_user_agent': 'FireFox',
     })
for each in urllist:
    art = g.extract(url=each)
    print '[文章标题]\n%s \n[内容描述]\n%s \n[正文内容]\n%s \n' % (art.title, art.meta_description, art.cleaned_text)
    # print art.title

# import requests
# from goose import Goose
# from goose.text import StopWordsChinese
# from lxml import etree
# import chardet
# from datetime import datetime
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf8')


import urllib2
# import goose
# # url = "http://www.nytimes.com/2013/08/18/world/middleeast/pressure-by-us-failed-to-sway-egypts-leaders.html?hp"
# url = 'http://news.sina.com.cn/c/2017-09-30/doc-ifymkxmh8098151.shtml'
# req = requests.get(url)
# raw_html = req.content
#
# g = goose.Goose({'stopwords_class': StopWordsChinese})
# a = g.extract(raw_html=raw_html)
# print a.cleaned_text