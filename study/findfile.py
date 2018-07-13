#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/12 15:51
# @Author  : 疏影
# @File    : findfile.py
import os

class file():
    def __init__(self,rootdir):
        self.rootdir = rootdir
        self.filelst =[]

    def show_name(self):
        '''显示当前路径下的所有文件'''
        filelst = []
        if os.path.exists(self.rootdir):
            for root, dirs, files in os.walk(self.rootdir):
                for f in files:
                    path = os.path.join(root, f).decode('gbk')
                    filelst.append({
                        'filename':os.path.basename(path),
                        'path':path})
        else:
            print u'路径不存在'
        self.filelst = filelst

    def find_file(self,file_name):
        if len(self.filelst)>0:
            for item in self.filelst:
                if file_name == item['filename']:
                    return item['path']

if __name__ == '__main__':
    rootdir = r'E:\tempTest'
    file = file(rootdir)
    file.show_name()