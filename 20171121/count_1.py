# coding:utf-8

# -*- coding: utf-8 -*-
import xdrlib, sys
import xlrd,xlwt

def open_excel(file='file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)

# 根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file='C:\Users\syph\Desktop/11.xlsx', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[0]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []
    for rownum in range(1, nrows):

        row = table.row_values(rownum)
        if row:
            # app = {}
            for i in range(len(colnames) - 1):
                # app[colnames[i]] = row[i]
                list.append(row[i])
    return list


def main():
    tables = excel_table_byindex()
    # print tables
    # for row in tables:
    #     print row
    # count_times = []
    # for j in tables:
    #     print tables.count(j)
    d = {}
    for row in tables:
        d[row] = tables.count(row)
    for key in d:
        t = {}
        t[key] = d[key]
        print(t)



if __name__ == "__main__":
    main()
    # write('C:\Users\syph\Desktop/

