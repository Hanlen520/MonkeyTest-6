#!/user/bin/env python
# -*- coding:utf-8 -*-
import xlrd
from config import *

def read_file(file_path):
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheets()[0]            # 打开第一个sheet
    print sheet.nrows,sheet.ncols           # 获取行列数

    http_list = []
    # [u'No', u'Type', u'Interface', u'Params']
    excel_title = sheet.row_values(0)
    for i in range(1,sheet.nrows):
        row_content= sheet.row_values(i)
        dict1 = dict(zip(excel_title, row_content))
        http_list.append(dict1)

    return http_list

def get_fun(path,params):
    url = URL + path
    t = Tool()
    if not params:
        new_data = t.signfun({})
    response = requests.get(url=url,headers=HEADER_IOS,params=new_data)

    if 200 == response.status_code:
        print "响应结果：",response.content.decode("unicode-escape")
    else:
        print response.status_code

if __name__ == '__main__':
    file = 'http.xls'
    http_list = read_file(file)

    print http_list

    for row in http_list:
        if 'get'==row['Type']:
            get_fun(row['Interface'],row['Params'])