import pandas as pd
import pymssql


host = "127.0.0.1"
username = 'sa'
pwd = 'Tingche.easy'
db = 'Tingche.easyDB'
port = 433
charset = 'utf8'
xls_name = 'test.xlsx'

# 连接数据库
def conn2SQL():
    conn = pymssql.connect(host, username, pwd, db)
    sql_1 = '''select * from table where
    '''
    data = pd.read_sql(sql_1,conn)
