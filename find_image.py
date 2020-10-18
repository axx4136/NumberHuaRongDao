import base64
import os
from PIL import Image
import numpy as np
import cutImage as c
fileList=os.listdir('./picture')
#找到题目图片对应的字母
def find_image():
    for dir in fileList:#遍历题目库
        count = 0
        fileName=[]
        picList=os.listdir('./picture/'+dir)
        for p in os.listdir('./QuestionCut'):#遍历题目切图的9张
            for pic in picList:#遍历dir下的所有图片
                with open('./QuestionCut/'+p, 'rb') as f1:
                    base64_problem = base64.b64encode(f1.read())
                with open('./picture/'+dir+'/'+pic,'rb') as f:
                    base64_data=base64.b64encode(f.read())
                if base64_data==base64_problem:#两张图片相同
                    count=count+1
        if count==8:#除了空白的图，如果有八张图片相同，定位到这个字母
            return dir
#创建二维数组，一位数组，找到空格的数字和位置
def make_qipan(m):
    sign=[1,2,3,4,5,6,7,8,9]#存储被挖空的图的位置
    blanknumber=[1,2,3,4,5,6,7,8,9]#存储被挖空的图是第几张图
    temp=[]#存储棋盘的顺序
    qipan=np.arange(1,10).reshape(3,3)#创建2维数组
    for pic2 in os.listdir('./QuestionCut'):
        for pic1 in os.listdir('./picture/' +m):
            with open ('./picture/'+m+'/'+pic1,'rb') as f1:
                base64_f1=base64.b64encode(f1.read())
            with open ('./QuestionCut/'+pic2,'rb') as f2:
                base64_f2=base64.b64encode(f2.read())
            if base64_f1==base64_f2:#找到切图和数据库中的对应关系
                number=int(pic2.split('.')[0])
                col=(number-1)%3#记录每一个问题切图的所在列
                row=int((number-1)/3)#记录每一个问题切图的所在行
                qipan[row][col]=pic1.split('.')[0]#对应棋盘的位置为这个图所对应数据库的图的数字
                temp.append(int(pic1.split('.')[0]))#按顺序存到temp
                sign.remove(number)#在存储被挖空的图的位置列表去除对应
                blanknumber.remove(int(pic1.split('.')[0]))#在存储被挖空的图的数字列表去除对应
    qipan[int((sign[0]-1)/3)][(sign[0]-1)%3]=blanknumber[0]#令二维数组被挖空的图的位置值为0
    return temp,qipan,sign[0],blanknumber[0]
#判断是否有解
def judgment(temp):
    signal=0
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            #计算逆序对
            if temp[i]>temp[j]:
                signal+=1
                #保存第一个有逆序对的数字的位置
                if signal==1:
                    position=i
    if signal%2!=0:#逆序对为奇数则无解
        print('no way')
        return signal,position
#自行交换
def swap(qipan,p,bkp):
    if bkp<=p: #空格在第一个逆序数的左边
        t = qipan[(p+1) // 3][(p+1) % 3]
        qipan[(p+1) // 3][(p+1) % 3] = qipan[(p + 2) // 3][(p + 2) % 3]
        qipan[(p + 2) // 3][(p + 2) % 3] = t
        print('swap[%d , %d]' % (p+1, p + 2))
        return p+1, p + 2
    else:
        if bkp==p+1:
            t=qipan[p//3][p%3]
            qipan[p//3][p%3]=qipan[(p+2)//3][(p+2)%3]
            qipan[(p + 2) // 3][(p + 2) % 3]=t
            print('swap[%d , %d]' % (p, p + 2))
            return p, p + 2
        else:
            t=qipan[p//3][p%3]
            qipan[p // 3][p % 3] = qipan[(p + 1) // 3][(p + 1) % 3]
            qipan[(p + 1) // 3][(p + 1) % 3] = t
            print('swap[%d , %d]' % (p, p + 1))
            return p, p + 1
#将除了被挖空的图的棋盘顺序导入列表
def turnToarray(qipan,bk):
    t=[]
    for i in range(3):
        for j in range(3):
            if qipan[i][j]!=bk:
                t.append(qipan[i][j])
    return t
#将包括被挖空的图导入列表
def turnToarray_1(qipan):
    t=[]
    for i in range(3):
        for j in range(3):
                t.append(qipan[i][j])
    return t
m=find_image()
numberarray,board,blank,bk=make_qipan(m)
array=turnToarray_1(board)
print(array)
print(turnToarray(board,bk))
print(blank)
print(m)