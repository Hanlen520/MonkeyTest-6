#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/2 10:42
# @Author  : 疏影
# @File    : 20180702.py

# 切片练习
def slice_fun():
    lst = list(range(100))
    # 索引从0开始，倒数第一个是-1
    print u'取前10个:', lst[:10]
    print u'取前10个:',lst[0:10]
    print u'取最后一个:',lst[-1]
    print u'取最后10个:',lst[-10:]
    print u'取倒数第6个到倒数第3个:', lst[-6:-3]

    print u'创造一个相同的', lst[:]
    print u'相反的', lst[::-1]

    print u'所有的数中，每2个数取一个', lst[::2]
    print u'前10个中，每3个数取一个', lst[:10:3]

# 列表练习
def list_fun():
    list = [1, 8, 8, 2, 3, 7, 4, 5, 6, 7, 8, 9]

    list.append(10)
    print u'追加后：',list

    # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    del_value = list.pop(4)
    print u'移除的值：',del_value,u',移除后：',list

    # 将对象插入列表
    list.insert(2,[45,8])
    print list

    # 在列表末尾添加新的对象
    list.append(7)
    print list

    # 移除列表中某个值的第一个匹配项
    list.remove(8)
    print list

    # 反向列表中元素
    list.reverse()
    print list

# 取1-100奇偶数
def jo_fun():
    jilst,oulist = [],[]
    for i in list(range(1,101)):
        if 0 != i % 2:
            jilst.append(i)
        else:
            oulist.append(i)

    print u'奇数：',jilst
    print u'偶数：',oulist

# 字典练习
def dict_fun():
    dict1 = {'no': '1', 'name': 'xiaozhang', 'age': '20'}
    print u'获取所有关键字：',dict1.keys()
    print u'获取所有值', dict1.values()

    # 遍历字典
    for key,value in dict1.items():
        print key,value
    # 如果键在字典dict里返回true，否则返回false
    if dict1.has_key('sex'):
        print u"dict1中有存在关键字sex"
    else:
        print u"不存在"

    # 把字典dict2的键 / 值对更新到dict里
    dict1.update({'sex':'man'})
    print dict1

if __name__ == '__main__':
    # slice_fun()
    # list_fun()
    # jo_fun()
    dict_fun()