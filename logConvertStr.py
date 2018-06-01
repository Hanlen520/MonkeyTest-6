#!/user/bin/env python
# -*- coding:utf-8 -*-

class logconver(object):
    def __init__(self):
        pass

    def logConvertStr(self,content,charset='utf-8'):
        """常用于日志中文乱码如‘\xe4\xba\xa7’
        转换为指定字符编码，常用字符集编码有utf-8，utf-8，gbk，gb2312等"""
        content = str(content).decode(charset)
        return content

# if __name__ == '__main__':
#     logConvertStr("[{u'title': u'\u7528\u6237\u5c3e\u53f75245\u521a\u521a\u5356\u51fa\u4e00\u90e8iPhone 6s\u83b7\u5"
#                   "f971450\u5143'}, {u'title': u'\u7528\u6237\u5c3e\u53f74424\u521a\u521a\u5356\u51fa\u4e00\u90e8iPhone"
#                   " 6\u83b7\u5f97650\u5143'}, {u'title': u'\u7528\u6237\u5c3e\u53f74129\u521a\u521a\u5356\u51fa\u4e00\
#                   u90e8Galaxy S9\u83b7\u5f972800\u5143'}, {u'title': u'\u7528\u6237\u5c3e\u53f71190\u521a\u521a\u5356\u"
#                   "51fa\u4e00\u90e8iPhone 6 Plus\u83b7\u5f971600\u5143'}, {u'title': u'\u7528\u6237\u5c3e\u53f77064\u521a"
#                   "\u521a\u5356\u51fa\u4e00\u90e8iPhone 7 Plus\u83b7\u5f972500\u5143'}]",charset='unicode-escape')