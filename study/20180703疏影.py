#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/5 9:43
# @Author  : 疏影
# @File    : 20180703疏影.py

# 1. 九九乘法表
def multi_fun():
    for i in range(1,10):
        for j in range(1, i + 1):
            a = i * j
            print i,'x',j,'=',a,'\t',
        print ""

# 2.  1,2,3,4数字，能组成多少个互不相同无重复数字的三位数，分别是多少?
def com_fun(list):
    for x in list:
        for y in list:
            for z in list:
                if (x != y) and (y != z) and (z != x):
                    # print x, y, z
                    print('%d%d%d'%(x,y,z)),

if __name__ == '__main__':
    print u'九九乘法表:'
    multi_fun()
    list=[1,2,3,4]
    print list,'互不相同无重复数字的三位数，分别是:'
    com_fun(list)