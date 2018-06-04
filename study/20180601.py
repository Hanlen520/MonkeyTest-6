#!/user/bin/env python
# -*- coding:utf-8 -*-
import time
import datetime
import calendar

if __name__ == '__main__':
    now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    print now
    #
    # print time.localtime(time.time())
    #
    # print time.strptime('20180601145525','%Y%m%d%H%M%S')
    #
    # # 使用datetime模块来获取当前的日期和时间
    # print datetime.datetime.now()
    # 输出2018年6月份的日历
    print calendar.month(2018,6)

    # 返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21 * W + 18 + 2 * C。l是每星期行数。
    print calendar.calendar(2018,w=2,l=1,c=6)