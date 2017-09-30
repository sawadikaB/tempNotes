# !/usr/bin/env python
# -*- coding=utf-8 -*-

_version_ = 1.0

import sys
reload(sys); sys.setdefaultencoding('utf-8')
import goose
from rpcgoose_Worker import Worker

class goose_Engine():

    def __init__(self):
        self.worker = Worker()

    # 假设直接获取到url了已经
    def _getcontent(self, urllist):
        if isinstance(urllist, list):
            for each in urllist:
                pass

        else:
            return
