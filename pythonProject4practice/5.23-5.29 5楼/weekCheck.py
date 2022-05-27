import os
import pandas as pd
import xlrd
import docxtpl

if __name__ == '__main__':
    # 当前文件路径
    file = os.path.realpath(__file__)
    print(file)
    # 当前文件所在的目录，即父路径
    proDir = os.path.split(os.path.realpath(__file__))[0]
    print(proDir)
    # 找到父路径下的其他文件，即同级的其他文件
    file = (os.path.join(proDir, "租赁销售汇总导出.csv"))

    shop_list = []
    for root, dirs, files in os.walk(proDir):
        for f in files:
            if os.path.splitext(f)[1] == '.jpg':
                shop_list.append(f.split('.')[0])
    print(shop_list)



    data = pd.read_csv(file, encoding='gbk')
    shop_id = data["铺位号"].str.rstrip()
    shop_name = data["品牌"].str.rstrip()
    shop_amount = data["小计销售"]

    context = []
    num = data.shape[0]
    for i in range(num):
        for n in shop_list:
            if n in shop_name[i]:
                context.append({
                    "铺位号":shop_id[i],
                    "品牌":shop_name[i].split('-')[1],
                    "小计销售":shop_amount[i]
                })
                break

    print(context)
    print(len(context))

    for shop_dict in context:
        print(shop_dict['铺位号'])
        print(shop_dict['品牌'])
        print(shop_dict['小计销售'])

