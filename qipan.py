import numpy as np
from prediction import Prediction
import base64
import json
import requests
import find_image as f
import sys

class Qipan:
    def __init__(self):
        self.n = 3
        self.N = self.n * self.n
        self.init = np.arange(1, self.N + 1).reshape(self.n, self.n)
        self.qipan = self.init.copy()
        self.bk_x = (f.blank-1)//3
        self.bk_y = (f.blank-1)%3
        self.bk_x_p = -1
        self.bk_y_p = -1
        self.pre = Prediction()
        self.started = False  # 标记是否开始
        self.X = [-1, 0, 1, 0]
        self.Y = [0, -1, 0, 1]
        self.answer=""
        self.ForceStep=f.c.URL.Step
        self.ForceSwap=f.c.URL.Swap
        self.uuid=""
        self.autoswap1=-1
        self.autoswap2=-1
    def scan_qipan(self):
        self.qipan=np.array(f.array).reshape(3,3)
        self.bk_x_p=-1
        self.bk_y_p=-1
        self.step=0
        self.started=True
    def move(self, x, y):  # 移动棋子
        if x < 0 or x >= self.n or y < 0 or y >= self.n:
            return
        self.qipan[self.bk_x][self.bk_y] = self.qipan[x][y]
        self.qipan[x][y] = f.bk
        self.bk_x_p = self.bk_x
        self.bk_y_p = self.bk_y
        self.bk_x = x
        self.bk_y = y

    def is_finish(self):  # 判断游戏是否结束
        for i in range(self.n):
            for j in range(self.n):
                if self.qipan[i][j] != self.init[i][j]:
                    return False
        return True

    def show(self):  # 打印当前棋盘状态
        s = ""
        for i in range(self.n):
            for j in range(self.n):
                #空白
                if self.qipan[i][j] == f.bk:
                    s += "  "
                else:
                    s += str(self.qipan[i][j]) + " "
            s += "\n"
        print(s)

    def tips(self):  # 提示一步
        if self.step==self.ForceStep:
            swap1_x=(int(self.ForceSwap[0])-1)//3
            swap1_y=(int(self.ForceSwap[0])-1)%3
            swap2_x = (int(self.ForceSwap[1]) - 1) // 3
            swap2_y = (int(self.ForceSwap[1]) - 1) % 3
            t = self.qipan[swap1_x][swap1_y]
            self.qipan[swap1_x][swap1_y] = self.qipan[swap2_x][swap2_y]
            self.qipan[swap2_x][swap2_y] = t
            print("强制交换 [%d,%d]   [%d,%d]" %(swap1_x,swap1_y,swap2_x,swap2_y))
            self.show()
            if swap1_x==self.bk_x and swap1_y==self.bk_y:
                self.bk_x=swap2_x
                self.bk_y=swap2_y
                self.bk_x_p=-1
                self.bk_y_p=-1
            elif swap2_x==self.bk_x and swap2_y==self.bk_y:
                self.bk_x = swap1_x
                self.bk_y = swap1_y
                self.bk_x_p = -1
                self.bk_y_p = -1
            if f.judgment(f.turnToarray(self.qipan,f.bk)) is not None:
                list=f.turnToarray(self.qipan, f.bk)
                flag,p=f.judgment(list)
                if flag%2!=0:
                    bkp_1=self.bk_x*3+self.bk_y
                    self.autoswap1,self.autoswap2=f.swap(self.qipan,p,bkp_1)
            self.show()
        i = self.pre.pre_next(self.qipan, self.bk_x, self.bk_y, self.bk_x_p, self.bk_y_p)
        if i==0:
            self.answer=self.answer+"w"
        if i==1:
            self.answer=self.answer+"a"
        if i==2:
            self.answer=self.answer+"s"
        if i==3:
            self.answer=self.answer+"d"
        x = self.bk_x + self.X[i]
        y = self.bk_y + self.Y[i]
        self.move(x, y)
        self.step += 1
        print("step", self.step)
        self.show()
qi = Qipan()
qi.scan_qipan()
Step=0
qi.show()
while not qi.is_finish():
    qi.tips()
    Step+=1
operations=qi.answer
swaplist=[]
if qi.autoswap1+1!=0:
    swaplist.append(qi.autoswap1+1)
    swaplist.append(qi.autoswap2+1)
print(swaplist)
#print("uuid:"+f.c.URL.Uuid)
print("operation:"+qi.answer)
print("swap:[%d,%d]" %(qi.autoswap1+1,qi.autoswap2+1))
print("step:%d" %(Step))