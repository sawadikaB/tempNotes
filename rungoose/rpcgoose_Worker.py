# !/usr/bin/env python
# -*- coding:utf-8 -*-
_version_ = 1.0

from goose import Goose
from goose.text import StopWordsChinese
from rpcgoose_setting import HEADERS
import requests

class Worker():

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def _goose_getcontent(self, content, dealtype):
        '''

        :param content: goose接受的对象，可以是url或者html
        :param dealtype: 处理方式，1为url处理，其他的为html处理，默认为1
        :return:
        '''
        g = Goose({
            'stopwords_class': StopWordsChinese,
            'browser_user_agent': 'FireFox', # 后面再封装一下 不要写死，这是一个功能，可随机更换ua头
         })
        if dealtype == 1:
            art = g.extract(url=content)
        else:
            art = g.extract(raw_html=content)
        return art.title, art.cleaned_text
        # print art.title

    # def _goose_hardget(self, html):
    #     '''
    #     某些网站需要cookie，goose无法获取，可以先用requests拿到html给goose解析
    #     :param: 页面html
    #     :return:
    #     '''
    #     g = Goose({
    #         'stopwords_class': StopWordsChinese,
    #     })
    #     art = g.extract(raw_html=html)
    #     return art.title, art.cleaned_text
    #     # print art.title

    def _html_get(self, url, pagecode):
        '''
        :param url:需要获取的页面url
        :return: (str)html
        '''
        try:
            res = self.session.get(url)
            html = res.content.decode(pagecode)
        except Exception:
            error = 'html页面获取出错'
            html = 'no_data'
        return html

    def usegoose(self, content, dealtype=1):
        return self._goose_getcontent(content, dealtype)

    def getcontent(self, url, pagecode='utf-8'):
        return self._html_get(url, pagecode)



