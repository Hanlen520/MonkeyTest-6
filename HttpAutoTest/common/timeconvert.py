#!/user/bin/env python
# -*- coding:utf-8 -*-
import time
import datetime

if __name__ == '__main__':
    # 日期格式化
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print now
    print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print type(now)

    # 秒级时间戳（浮点数）
    print time.time()
    # 秒级
    print int(time.time())

    # 转换成时间数组
    timeArray = time.strptime(now, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳（浮点数）
    timestamp = time.mktime(timeArray)
    print timestamp

    now_time = time.localtime(time.time())
    # 获取当前时间的年
    print now_time
    print now_time.tm_year
