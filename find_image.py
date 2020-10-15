import base64
import os
from PIL import Image
import numpy as np
import cutImage as c
fileList=os.listdir('./picture')
def find_image():
    for dir in fileList:
        count = 0
        fileName=[]
        picList=os.listdir('./picture/'+dir)
        for p in os.listdir('./QuestionCut'):
            for pic in picList:
                with open('./QuestionCut/'+p, 'rb') as f1:
                    base64_problem = base64.b64encode(f1.read())
                with open('./picture/'+dir+'/'+pic,'rb') as f:
                    base64_data=base64.b64encode(f.read())
                if base64_data==base64_problem:
                    count=count+1
        if count==8:
            return dir
def make_qipan(m):
    sign=[1,2,3,4,5,6,7,8,9]
    blanknumber=[1,2,3,4,5,6,7,8,9]
    temp=[]
    qipan=np.arange(1,10).reshape(3,3)
    for pic2 in os.listdir('./QuestionCut'):
        for pic1 in os.listdir('./picture/' +m):
            with open ('./picture/'+m+'/'+pic1,'rb') as f1:
                base64_f1=base64.b64encode(f1.read())
            with open ('./QuestionCut/'+pic2,'rb') as f2:
                base64_f2=base64.b64encode(f2.read())
            if base64_f1==base64_f2:
                number=int(pic2.split('.')[0])
                col=(number-1)%3
                row=int((number-1)/3)
                qipan[row][col]=pic1.split('.')[0]
                temp.append(int(pic1.split('.')[0]))
                sign.remove(number)
                blanknumber.remove(int(pic1.split('.')[0]))
    qipan[int((sign[0]-1)/3)][(sign[0]-1)%3]=blanknumber[0]
    return temp,qipan,sign[0],blanknumber[0]
def judgment(temp):
    signal=0
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            if temp[i]>temp[j]:
                signal+=1
            if signal==1:
                position=i
    if signal%2!=0:
        print('no way')
    return signal,position
def swap(qipan,p):
    print('swap[%d , %d]' % (p+1, p+2))
    if p==0:  #交换的第一个数为第一格
        if qipan[(p+1)//3][(p+1)%3]==bk:#如果下一格为挖去的格子
            tempnumber=qipan[p//3][p%3]
            qipan[p//3][p%3]=qipan[(p+2)//3][(p+2)%3]
            qipan[(p + 2) // 3][(p + 2) % 3]=tempnumber
        else:
            tempnumber = qipan[p // 3][p % 3]
            qipan[p // 3][p % 3] = qipan[(p + 1) // 3][(p + 1) % 3]
            qipan[(p + 1) // 3][(p + 1) % 3] = tempnumber
    else:
        if qipan[(p+1)//3][(p+1)%3]==bk:#如果下一格为挖去的格子
            tempnumber = qipan[p // 3][p % 3]
            qipan[p // 3][p % 3] = qipan[(p + 2) // 3][(p + 2) % 3]
            qipan[(p + 2) // 3][(p + 2) % 3] = tempnumber
        elif p>=blank:#空格在交换的位置之前
            tempnumber = qipan[(p + 1) // 3][(p + 1) % 3]
            qipan[(p + 1) // 3][(p + 1) % 3] = qipan[(p + 2) // 3][(p + 2) % 3]
            qipan[(p + 2) // 3][(p + 2) % 3] = tempnumber
        else:
            tempnumber = qipan[p // 3][p % 3]
            qipan[p // 3][p % 3] = qipan[(p + 1) // 3][(p + 1) % 3]
            qipan[(p + 1) // 3][(p + 1) % 3] = tempnumber
def turnToarray(qipan,bk):
    t=[]
    for i in range(3):
        for j in range(3):
            if qipan[i][j]!=bk:
                t.append(qipan[i][j])
    return t
def turnToarray_1(qipan):
    t=[]
    for i in range(3):
        for j in range(3):
                t.append(qipan[i][j])
    return t
m=find_image()
numberarray,board,blank,bk=make_qipan(m)
s,pos=judgment(numberarray)
if s%2!=0:
    swap(board,pos)
array=turnToarray_1(board)
print(array)
print(turnToarray(board,bk))
print(blank)
print(m)