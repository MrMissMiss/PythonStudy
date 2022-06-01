import threading
import tkinter
from time import sleep

import schedule

event = threading.Event()

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

class GUI:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Test')
        self.root.geometry("500x200+1100+150")
        self.interface()

    def interface(self):
        """界面编写位置"""
        self.t = tkinter.Text(self.root, width=40, height=3)
        self.t.place(x=10, y=10)
        self.b0 = tkinter.Button(self.root, text='测试客流', width=10, height=1, command=self.start)
        self.b0.place(x=10, y=60)
        self.b1 = tkinter.Button(self.root, text='终端状态', width=10, height=1, command=self.stop)
        self.b1.place(x=100, y=60)
        self.b2 = tkinter.Button(self.root, text='交换机状态', width=10, height=1, command=self.conti)
        self.b2.place(x=200, y=60)

    def event(self):
        """按钮时间，无限循环"""
        schedule.every().day.at(time_84).do(self.stop)  # 每天8点40终端状态检查
        schedule.every().day.at(time_84).do(self.stop)  # 每天8点40交换机检查
        schedule.every().day.at(time_17).do(self.stop)  # 每天17点终端状态检查
        schedule.every().day.at(time_17).do(self.stop)  # 每天17点交换机检查
        schedule.every().day.at(time_94).do(self.stop)  # 每天9点40点服务器检查
        schedule.every(0.1).minutes.do(self.run)  # 每隔一分钟执行一次任务
        while True:
            sleep(1)
            event.wait()
            # self.t.insert(1.0, '运行中\n')
            schedule.run_pending()

    def run(self):
        self.t.insert(1.0, '运行中\n')

    def start(self):
        event.set()
        self.Th = threading.Thread(target=self.event)
        self.Th.setDaemon(True)
        self.Th.start()

    def stop(self):
        event.clear()
        self.t.insert(1.0, '暂停\n')

    def conti(self):
        event.set()
        self.t.insert(1.0, '继续\n')

if __name__ == '__main__':
    a = GUI()
    a.root.mainloop()