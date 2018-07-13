#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/12 15:51
# @Author  : 疏影
# @File    : findfile.py
import os
import time

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
                    filelst.append(os.path.join(root, f).decode('gbk'))
        else:
            print u'路径不存在'
        self.filelst = filelst

    def find_file(self,file_name):
        self.show_name()
        file_path = [] # 不同路径下有相同的文件
        if len(self.filelst)>0:
            for item in self.filelst:
                if file_name == os.path.basename(item):
                    file_path.append(item)
        else:
            print u'路径不存在'
        return file_path

    def creat_file(self):
        ''' 当前目录下建立/result/时间戳文件夹 '''
        now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        print now

        dir_path = os.path.join(os.getcwd(),'result')
        time_dir_path = os.path.join(dir_path,now)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        if not os.path.exists(time_dir_path):
            os.mkdir(time_dir_path)

if __name__ == '__main__':
    rootdir = r'E:\tempTest'
    file = file(rootdir)
    file.show_name()
    print file.filelst

    print file.find_file('sdhh3.jmx')

    file.creat_file()