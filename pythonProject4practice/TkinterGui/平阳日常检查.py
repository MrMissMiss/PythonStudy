import datetime,time #定时
import schedule #定时
import pymssql #数据库
# from pymssql import _mssql
# from pymssql import _pymssql
import uuid
import decimal
import requests #webhook
import json #webhook
from configparser import ConfigParser
import sys, traceback
from pythonping import ping

#程序运行状态  true为运行中   false为停止
flag = False
#数据库地址
DATABASE_IP = '10.128.50.250\IPVA'
#数据库账号
DATABASE_USER = 'sa'
#数据库密码
DATABASE_PASS = 'ipva@07'
#数据库名 数据库名末尾根据年份变更，否则无法查询得到数据
DATABASE_NAME = 'IPVA_S0400_B1'
#同比相差多少天
#day_c=-354
# 定时发送的时间
time_11='11:00'
time_14='14:00'
time_16='16:00'
time_17='17:00'
time_20='20:00'
time_22='22:00'
#系统检查时间
time_84='08:40'
time_94='09:40'
# TODO 你的IP
server_list = [
    '11.11.11.1','10.255.255.1','10.255.255.2','10.255.255.3','10.255.255.11','10.255.255.15','10.255.255.16',
    '10.255.255.17','10.255.255.18','10.255.255.19','10.255.255.20','10.255.255.21','10.255.255.22','10.255.255.23',
    '10.255.255.24','10.255.255.25','10.255.255.27','10.255.255.28','10.255.255.29','10.255.255.30','10.255.255.31',
    '10.255.255.32','10.255.255.33','10.255.255.34','10.255.255.35','10.255.255.36','10.255.255.37','10.255.255.38',
    '10.255.255.39','10.255.255.40','10.255.255.41','10.255.255.42','10.255.255.43','10.255.255.44','10.255.255.45',
    '10.255.255.46','10.255.255.47','10.255.255.48','10.255.255.49','10.255.255.51','10.255.255.52','10.255.255.55',
    '10.255.255.100','10.128.50.250'
]
def jobfs(kl): #(钉钉发送)
    # webhook发送部分
    # 企业微信后台接口总
    url = 'https://oapi.dingtalk.com/robot/send?access_token=39208862f8c332d6a3c15e6e1dad94a6fb4165792b7ba957435aa50cf16c72ef'
    program = {
        "msgtype": "text",
        "text": {"content": kl}
    }
    headers = {'Content-Type': 'application/json'}
    f = requests.post(url, data=json.dumps(program), headers=headers)
    t.delete('1.0', 'end')  # 删除文本框里内容
    t.insert('insert', kl + '\n')
def job_fwq(): #9点客流服务器工作状态判断
    #获取当前时间
    today = datetime.datetime.now().strftime("%Y-%m-%d") #本日开始时间
    #数据库查询部分
    try:
        db = pymssql.connect(DATABASE_IP, DATABASE_USER, DATABASE_PASS, DATABASE_NAME)
        cursor = db.cursor()
    except:
        job_c()
    else:
        cursor.execute(
            "SELECT datekey as rq, sum(insum) as zl\
                FROM Summary_Sixty\
                    WHERE SiteKey in ('P00004') and CountDate BETWEEN '" + today + "' and '" + today + ' 23:59'"'\
                    AND CONVERT (CHAR(8), CountDate, 108) BETWEEN '00:00'AND '08:59' group by datekey")
        row_t1 = cursor.fetchone()
        db.close()
        kl="截止9点，平阳银泰城客流为 "+str(row_t1[1])+"\n"
        if int(row_t1[1]) >= 750 and int(row_t1[1]) <= 2000 :
            kl += "(测试客流数据范围750-2000)"
        else:
            kl += " 平阳银泰城客流数据异常，数据超出(750-2000)，请检查客流服务器状态"
        print(kl)
        jobfs(kl)
def job_zt(): #客流终端在线查询
    today_to = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #数据库查询当前客流终端分析盒子情况，超过20分钟的终端
    try:
        db = pymssql.connect(DATABASE_IP, DATABASE_USER, DATABASE_PASS, DATABASE_NAME)
        cursor = db.cursor()
    except:
        job_c()
    else:
        cursor.execute("SELECT top 45 substring([设备点码],1,Charindex('.',[设备点码])-1) 设备,[通道号],[延迟时长(小时)],CONVERT(nvarchar(100),[状态]),CONVERT(nvarchar(100),[处理建议])\
                        FROM View_DataReportingStatusQuery WHERE [状态值] !='1'")
        rows = cursor.fetchall()
        db.close()
        kl = "-----客流终端故障状态检查-----\n"
        if len(rows) <= 0 :
            kl +=  today_to+" 平阳银泰城-客流分析终端无异常！"
        else:
            kl +=  today_to+" 平阳银泰城有"+ str(len(rows))+"个客流通道异常：\n"
            #统计异常终端的明细
            for i in range(0, len(rows),1):
                kl += str(i+1) + "-终端:" + str(rows[i][0]) +"通道:"+ str(rows[i][1])+"未上报:" + str(rows[i][2]) + "小时,状态:"+rows[i][3]+",处理意见:"+rows[i][4]+",\n"
            kl += "以上异常，请尽快检查！！！"
        print(kl)
        jobfs(kl)
def main():
    print('开始运行')
    error_list = []

    for ip in server_list:
        rs = ping(ip, verbose=True,timeout=2,count=1)
        if 1 <= rs.rtt_avg <= 2:
            # TODO 发送到钉钉
            text = f'交换机{ip} ping 超时 {rs.rtt_avg}\n'
            jobfs(text)
            error_list.append(ip)
            pass

    if len(error_list) == 0:
        text = f'交换机一切正常\n'
        jobfs(text)
    print('结束')
    pass
def job_c(): #数据库连接异常排查
    kl='测试--数据库连接失败，请检查客流服务器状态'
    jobfs(kl)

#窗口
import tkinter as tk  # 使用Tkinter前需要先导入
# 第1步，实例化object，建立窗口window
window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title('平阳银泰城日常检查')
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('300x150')  # 这里的乘是小x
t = tk.Text(window, width=40, height=3)
t.place(x=10, y=10)
b0 = tk.Button(window, text='测试客流', width=10, height=1, command=lambda:job_fwq())
b0.place(x=10, y=60)
b1 = tk.Button(window, text='终端状态', width=10, height=1, command=job_zt)
b1.place(x=100, y=60)
b2 = tk.Button(window, text='交换机状态', width=10, height=1, command=main)
b2.place(x=200, y=60)
# b3 = tk.Button(window, text='运行', width=10, height=1, command=running)
# b3.place(x=10, y=100)
# b4 = tk.Button(window, text='停止', width=10, height=1, command=stop)
# b4.place(x=100, y=100)

if __name__ == '__main__':
# 定时发送部分
    #系统检查
    schedule.every().day.at(time_84).do(job_zt) #每天8点40终端状态检查
    schedule.every().day.at(time_84).do(main) #每天8点40交换机检查
    schedule.every().day.at(time_17).do(job_zt) #每天17点终端状态检查
    schedule.every().day.at(time_17).do(main) #每天17点交换机检查
    schedule.every().day.at(time_94).do(job_fwq) #每天9点40点服务器检查
    schedule.every(0.1).minutes.do(main) #每隔一分钟执行一次任务
    while True:
        schedule.run_pending()
        time.sleep(1)
        #第8步，主窗口循环显示
        window.mainloop()