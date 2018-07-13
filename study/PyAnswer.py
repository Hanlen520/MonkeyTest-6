# coding=utf-8
import os,time,datetime,json
#1.请写出一段python代码实现删除一个list里边的重复元素
'''
#方法一：
s=[1,1,4,5,6,7,7,7,8]
h=set(s)
print [i for i in h]
print list(h)

s=[1,1,4,5,6,7,7,7,8]
#方法二：
b={}
b=b.fromkeys(s)  #字典函数没有相同的key
print b
c=list(b.keys())
print c
'''
#2.对str1='Hello World'实现字符串翻转,请用两种方式
'''
#方法一：
str1='Hello World'
print str1[::-1]

#方法二：
s=list(str1)
s.reverse()  #对列表进行反转
print s
new_str=''.join(s)  #将列表转成字符串
print new_str
'''
#3.输入一个日期(格式：yyyy-mm-dd)并且计算该日期是那年的第几天,假定给的日期是正确的
'''
#方法一：
def get_day(day):
    s=time.strptime(day,"%Y-%m-%d")
    print s
    print s.tm_yday  #格式化输出的直接拿出是第几天
get_day("2017-11-21")
'''
'''
#方法二：
def is_leap_year(year): # 判断闰年，是则返回True，否则返回False
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False
def function1(day): # 计算给定日期是那一年的第几天
  str1=day.split('-')  #通过‘-’进行分割，得到列表
  year=int(str1[0])
  month=int(str1[1])
  day=int(str1[2])

  leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  no_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap_year(year):
    #
    result = sum(leap_year[:month - 1]) + day
  else:
    result = sum(no_leap_year[:month - 1]) + day
  return result
print function1("2017-11-21")
'''
'''
get_day("2018-04-21")

#把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d-%H")

#把字符串转成datetime
def string_toDatetime(string):
    return datetime.strptime(string, "%Y-%m-%d-%H")

#把字符串转成时间戳形式
def string_toTimestamp(strTime):
    return time.mktime(string_toDatetime(strTime).timetuple())

#把时间戳转成字符串形式
def timestamp_toString(stamp):
    return time.strftime("%Y-%m-%d-%H", time.localtime(stamp))

#把datetime类型转外时间戳形式
def datetime_toTimestamp(dateTim):
    return time.mktime(dateTim.timetuple())
'''
#4.输入一个文件夹地址，遍历这个文件夹内所有文件并以：文件名字：文件详细地址，为字典进行保存
'''
s=dict()
def get_dict(folder):
    for file_name in os.listdir(folder):
        file_name=file_name.decode('gbk')
        path=os.path.join(folder,file_name)
        s[file_name]=path

get_dict("C:\Users\Jack\Desktop\class\ppt")
t=json.dumps(s,ensure_ascii=False)
print t
'''
'''
#os.path.abspath(path) #返回绝对路径
#os.path.basename(path) #返回文件名
#os.path.commonprefix(list) #返回多个路径中，所有path共有的最长的路径。
#os.path.dirname(path) #返回文件路径
#os.path.exists(path)  #路径存在则返回True,路径损坏返回False

#os.path.expanduser(path)  #把path中包含的"~"和"~user"转换成用户目录
#os.path.expandvars(path)  #根据环境变量的值替换path中包含的”$name”和”${name}”
#os.path.getatime(path)  #返回最后一次进入此path的时间。
#os.path.getmtime(path)  #返回在此path下最后一次修改的时间。
#os.path.getctime(path)  #返回path的大小
#os.path.getsize(path)  #返回文件大小，如果文件不存在就返回错误
#os.path.isabs(path)  #判断是否为绝对路径
#os.path.isfile(path)  #判断路径是否为文件
#os.path.isdir(path)  #判断路径是否为目录
#os.path.islink(path)  #判断路径是否为链接
#os.path.ismount(path)  #判断路径是否为挂载点（）
#os.path.join(path1[, path2[, ...]])  #把目录和文件名合成一个路径
#os.path.normcase(path)  #转换path的大小写和斜杠
#os.path.normpath(path)  #规范path字符串形式
#os.path.realpath(path)  #返回path的真实路径
#os.path.relpath(path[, start])  #从start开始计算相对路径
#os.path.samefile(path1, path2)  #判目断录或文件是否相同
#os.path.sameopenfile(fp1, fp2)  #判断fp1和fp2是否指向同一文件
#os.path.samestat(stat1, stat2)  #判断stat tuple stat1和stat2是否指向同一个文件
#os.path.split(path)  #把路径分割成dirname和basename，返回一个元组
#os.path.splitdrive(path)   #一般用在windows下，返回驱动器名和路径组成的元组
#os.path.splitext(path)  #分割路径，返回路径名和文件扩展名的元组
#os.path.splitunc(path)  #把路径分割为加载点与文件
#os.path.walk(path, visit, arg)  #遍历path，进入每个目录都调用visit函数，visit函数必须有3个参数(arg, dirname, names)，dirname表示当前目录的目录名，names代表当前目录下的所有文件名，args则为walk的第三个参数
#os.path.supports_unicode_filenames  #设置是否支持unicode路径名
'''
#5.使用while完成下边的图形
'''
#*
#**
#***
#****
#*****
#****
#***
#**
#*
i=1
x=4
while i<=9:
    if i<=5:
        print "*" * i
    elif i>5:
        print "*" *x
        x=x-1
    i=i+1
'''