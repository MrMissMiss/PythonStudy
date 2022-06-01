import queue
import random
import threading
import time
import tkinter

# from numpy.random.mtrand import rand


class GuiPart():
    def __init__(self, master, queue, endCommand):
        self.queue = queue
        self.text = tkinter.Text(master, width=70, height=10)
        self.text.grid(row=0, column=0, columnspan=3)
        self.bt0 = tkinter.Button(master, text='Start', command=endCommand)
        self.bt0.grid(row=1, column=0)
        self.bt1 = tkinter.Button(master, text='Pause', command=endCommand)
        self.bt1.grid(row=1, column=1)
        self.bt2 = tkinter.Button(master, text='Stop', command=endCommand)
        self.bt2.grid(row=1, column=2)

    def processIncoming(self):
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                print(msg)
            except queue.Empty:
                pass

class ThreadedClient():
    def __init__(self,master):
        self.master = master
        self.queue = queue.Queue()
        self.gui = GuiPart(master,self.queue,self.endApplication)
        self.running = True
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()
        self.periodicCall()
    def periodicCall(self):
        self.master.after(200,self.periodicCall)
        self.gui.processIncoming()
        if not self.running:
            self.master.destroy()
    def workerThread1(self):
        # self.ott=tkinter.Tk()
        # self.ott.mainloop()
        while self.running:
            time.sleep(rand.random()*1.5)
            msg = rand.random()
            self.queue.put(msg)
    def endApplication(self):
        self.running = False

rand = random.Random()
root = tkinter.Tk()
client = ThreadedClient(root)
root.mainloop()