import os

import xlwt
import xlrd

# 导入文件
def get_file():
    """
    用于获取文件名
    :return: 返回值为文件名组成的列表
    """
    file_list = os.listdir('./')
    return file_list

# 保存生成Excel表
def load_data(file_list):
    """
    用于读取指定的文件并保存至字典数据结构中
    :param file_list:需要加载的文件列表
    :return:保存了文件内容的字典
    """
    dictory = {}
    for file in file_list:
        # 获取表格文件  打开xls文件
        wb = xlrd.open_workbook(file)
        # 抓取所有sheet页的名称
        wsheets = wb.sheet_names()
        # 定位到指定页（sheet1）
        ws1 = wb.sheet_by_name(u'sheet1')

    # 遍历sheet1中所有行row
    num_rows = ws1.nrows
    for curr_row in range(num_rows):
        row = ws1.row_values(curr_row)
        print(f'row {curr_row} is {row}')





def data2xls():
    pass