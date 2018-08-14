#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/7/24 11:38
# @Author  : 疏影
# @File    : zipTest.py
import zipfile
def fun1():
    azip = zipfile.ZipFile('F:\\httpAPITest.zip')

    # 返回所有文件夹和文件
    print(azip.namelist())
    # # 返回该zip的文件名
    print(azip.filename)

    # 压缩文件里bb文件夹下的aa.txt
    azip_info = azip.getinfo('httpAPITest/.classpath')
    # 原来文件大小
    print(azip_info.file_size)
    # 压缩后大小
    print(azip_info.compress_size)

    # 这样可以求得压缩率，保留小数点后两位
    print('压缩率为{:.2f}'.format(azip_info.file_size / azip_info.compress_size))

    # 可以直接读取里面的内容, 不过貌似是字节形式.需要解码回utf-8.参数也可以传ZiInfo, 如b
    a = azip.read('bb/cc.txt').decode('utf-8')
    print(a)
    # 打开文件再读取，好像比上面麻烦
    b = azip.open(azip_info)
    print(b.read().decode('utf-8'))
    azip.close()

if __name__ == '__main__':
    fun1()