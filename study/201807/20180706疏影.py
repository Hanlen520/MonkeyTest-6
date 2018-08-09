#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/6 10:30
# @Author  : 疏影
# @File    : 20180706疏影.py
import copy
import time
import datetime
import os

#1.请写出一段python代码实现删除一个list里边的重复元素
def del_list(lst):
    af_lst = []
    for item in lst:
        if item not in af_lst:
            af_lst.append(item)
    return af_lst

#2.对str1='Hello World'实现字符串翻转,请用两种方式
def str_rev1(str):
    str_aft = ''
    i = 0
    length = len(str)
    while i < length:
        str_aft += str[length-i-1]
        i += 1
    return str_aft

# 字符串转化数组,反转后再转换为字符串
def str_rev2(str):
    str_lst = list(str)
    str_lst.reverse()
    str_aft = ''.join(str_lst)
    return str_aft

# 使用切片
def str_rev3(str):
    # str_aft = copy.deepcopy(str)
    return str[::-1]

#3.输入一个日期(格式：yyyy-mm-dd)并且计算该日期是那年的第几天,假定给的日期是正确的
def date_count1(date):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[-2:])

    date1 = datetime.datetime(year, 1, 1)
    date2 = datetime.datetime(year, month, day)
    # toordinal()返回公元公历开始到现在的天数。公元1年1月1日为1
    return date2.toordinal() - date1.toordinal() + 1

def date_count2(str_date):
    a = time.strptime(str_date,"%Y-%m-%d")
    return a.tm_yday

#4.输入一个文件夹地址，遍历这个文件夹内所有文件并以：文件名字：文件详细地址，为字典进行保存
def file_list(rootdir,filelst):
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            filelst.append({'file_name':os.path.basename(path),'path':path})
        else:
            file_list(path,filelst)
    return filelst

#5.使用while完成下边的图形
def draw_fun():
    for i in range(1, 5):
        print i * '*'
    for i in range(5, 0, -1):
        print i * '*'

def get_dict(folder):
    s = dict()
    for file_name in os.listdir(folder):
        file_name=file_name.decode('gbk')
        path=os.path.join(folder,file_name)
        s[file_name]=path
    print s

def Test1(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            print os.path.join(root, d).decode('gbk')
        for f in files:
            print os.path.join(root, f).decode('gbk')

if __name__ == '__main__':
    # lst = [3,4,5,6,6,7,8,7,7,6,9,17,6]
    # print '删除前',lst
    # af_lst = del_list(lst)
    # print '删除后', af_lst

    # str_begin = 'Hello World'
    # print '翻转前', str_begin
    # str_aft1 =str_rev1(str_begin)
    # print '翻转后1', str_aft1
    # str_aft2 = str_rev2(str_begin)
    # print '翻转后2', str_aft2
    # str_aft3 = str_rev3(str_begin)
    # print '翻转后3', str_aft3

    # date = raw_input('输入一个日期(格式：yyyy-mm-dd):')
    # print '第%d天'%(date_count1(date))
    # print '第%d天' % (date_count2(date))

    # draw_fun()
    rootdir = r'E:\tempTest'
    # filelst=[]
    # filelst = file_list(rootdir,filelst)
    # print filelst

    # get_dict(rootdir)

    # 遍历某个文件下的所有文件
    # filelst = os.listdir(rootdir)
    # print filelst
    # for file in filelst:
    #     path = os.path.join(rootdir,file)
    #     if os.path.isfile(path):
    #         print file
    #
    # print os.getcwd()
    #
    # print os.path.exists(r'E:\temp1')

    Test1(rootdir)
