#!/user/bin/env python
# -*- coding:utf-8 -*-
import xlrd
def read_file(file_path):
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheets()[0]            # 打开第一个sheet
    print sheet.nrows,sheet.ncols           # 获取行列数

    dict2 = []
    excel_title = sheet.row_values(0)
    for i in range(1,sheet.nrows):
        row_content= sheet.row_values(i)
        dict1 = dict(zip(excel_title, row_content))
        dict2.append(dict1)
    print dict2

if __name__ == '__main__':
    file = 'http.xls'
    read_file(file)