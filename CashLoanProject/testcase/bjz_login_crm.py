#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/14 16:38
# @Author  : 疏影
# @File    : bjz_login_crm.py
import requests

def login():
    url = 'http://crm.xjd.51lianqian.net:7035/login'
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "max-age=0",
        "Content-Length":"79",
        "Content-Type":"application/x-www-form-urlencoded",
        "Cookie":"400-flush=eyJpdiI6InptbFdEdUpFaFQyXC90Y29YMGN2V1p3PT0iLCJ2YWx1ZSI6InhVMTJmcElQQmdcL21mR0d3VFU2YnBnPT0iLCJtYWMiOiJhOGJmM2UzZGVkOTAxOGVkMWZmMWJiOTA1MjExNDk2ZTdjY2EzYTFjNjE1NmI1YmQ0YzVlNTE5Y2Q0MzI1MmQ0In0%3D; XSRF-TOKEN=eyJpdiI6IlA0a3VpNlE3MGZUeXZ4cUxKSTFiOXc9PSIsInZhbHVlIjoiUVRWbzlBckhSZ2dmdXpzclZuc2NlNDRQOVJtNm9idTVwXC9QczgrV0VLbVFOOFljRFBvVWlGbG8xREMremlkaG12MFI2Q2hmemRXYkFuY0dVRE1RUGVnPT0iLCJtYWMiOiI2MGE0NjcxOWFjYzVmN2Q4Yjc0ODEzOWNmMjY0ODQ0MDRiNzRhMTIyMzc2YWI3OWRlMTcyMTI5NzAyMmY4NGVkIn0%3D; laravel_session=eyJpdiI6IjJiMTZMU2JLa0JHMmh1eTlmNjBZcGc9PSIsInZhbHVlIjoiSVozTzNoNlB0QWFqVlVockRGOThLOElMQUpDVDhFOSt4RXBNS0tDOEF1RmJ5OXBicUFBdUIxZTk2cWFHc2dLZ3Mxcmh2MUtTcFY4NndUQzBMVVMwQ1E9PSIsIm1hYyI6ImMwOTRmODQ4NjNkNzcxM2M3YjcyNDQyYTlmNzU0NGZiOWUwMTljZDdmNTllYjI1MjIzNzk3ZGIyOWE5YWIzMDcifQ%3D%3D",
        "Host": "bjzcrm.51mingyao.com",
        "Origin":"http://bjzcrm.51mingyao.com",
        "Proxy-Connection":"keep-alive",
        "Referer": "http://bjzcrm.51mingyao.com/login",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
    }
    b = '_token=BUR40ccY4IQ6mrRENkSJDYmk5M7WZ8rtYl01HmlO&name=lichengyan&password=abc123'

    reponse = requests.post(url,headers=header,data=b)
    print reponse
    # print reponse.content

if __name__ == '__main__':
    login()