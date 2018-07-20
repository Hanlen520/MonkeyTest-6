# coding=utf-8
import xlrd, os, sys
class Datas():
    def loginData(self):
        # 获取文件当前的目录相对路径
        self.cpath = os.path.dirname(sys.argv[0])
        # 获取当前文件上一层目录的相对路径
        self.dirpath = os.path.split( self.cpath)
        # 拼接到Public目录下的data.xlsx的路径
        try: # 情况一：双层级目录下 TestCase
            self.filename = self.dirpath[0] + '/Public/data.xlsx'
            #print(self.filename)
            self.data = xlrd.open_workbook(self.filename)
        except: # 情况二：直接项目文件目录下 run_casse
            self.filename = self.cpath + '/Public/data.xlsx'
            self.data = xlrd.open_workbook(self.filename)
        self.sheetname1 = "user_data"
        self.table = self.data.sheet_by_name(self.sheetname1)
        # 获取首行值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
        if self.rowNum <=1:
            pass
        else:
            r = []
            for i in range(1,self.rowNum):
                s = {}
                values = self.table.row_values(i)
                for x in range(0,self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
        username = int(r[0]['username'])
        password = str(r[0]['password'])
        return username, password

if __name__ == '__main__':
    Data =Datas()
    print(Data.loginData()[0])
    print(Data.loginData()[1])
