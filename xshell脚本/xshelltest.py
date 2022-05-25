import os
import re

global xsh

# xsh文件目录
file_dir = "C:\\Users\\cai\\Documents\\NetSarang Computer\\7\\Xshell\\Sessions"


def getFiles(path):
    for root, dirs, files in os.walk(file_dir):
        print("root_dir:", root)
        print("sub_dirs:", dirs)
        print("files:", files)
    return files


def runxsh(file_name):
    xshfile_path = "C:\\Users\\cai\\Documents\\NetSarang Computer\\7\\Xshell\\Sessions"
    xshfile_name = "\\" + file_name
    logfile_path = "E:\\python项目\\xshell脚本\\venv\\XshellLog"
    logfile_name = "\\" + file_name

    # 连接服务器
    xsh.Session.Open(xshfile_path + xshfile_name)
    xsh.Screen.Synchronous = True

    # 开始记录日志
    xsh.Session.LogFilePath = logfile_path + logfile_name
    xsh.Session.StartLog()
    xsh.Session.Sleep(1000)
    xsh.Screen.Send(" ")
    for i in range(100):
        last_Row = xsh.Screen.CurrentRow
        # xsh.Dialog.MsgBox('目前在第' + last_Row + '行')
        last_Words = xsh.Screen.Get(last_Row-1,0,last_Row-1,40)
        # xsh.Dialog.MsgBox('当前内容为' + last_Words)
        if re.match('.*return.*',last_Words) is not None:
            break
        if re.match('.*end.*',last_Words) is not None:
            break
        xsh.Screen.Send("    ")
        xsh.Session.Sleep(100)
    xsh.Screen.Send(" \n")
    xsh.Session.Sleep(1000)

    # 停止日志
    xsh.Session.StopLog()
    # 退出
    # xsh.Screen.Send("exit\n")
    # xsh.Screen.Send("quit\n")
    xsh.Session.Sleep(1000)
    # 关闭当前连接
    xsh.Session.Close()

    xsh.Session.Sleep(2000)


def Main():
    try:
        # 获取需要读取的所有文件list
        files_name = getFiles(file_dir)
        # skipfile_name 需要跳过的会话
        skipfile_name = ['10.129.99.12.xsh']
        parttern = ".*xsh"
        for file_name in files_name:
            # if file_name == '10.129.99.14.xsh':
            #     break
            if file_name in skipfile_name:
                continue
            res = re.match(parttern,file_name)
            if res is None:
                continue
            runxsh(file_name)
        xsh.Dialog.MsgBox('all sessions are completed!')
    except Exception as E:
        msg_e = 'execusion error-turn off' + str(E)
        xsh.Dialog.MsgBox(msg_e)

