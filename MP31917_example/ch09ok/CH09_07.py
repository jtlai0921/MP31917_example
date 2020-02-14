import random

INDEXBOX=7       #雜湊表元素個數
MAXNUM=13        #資料個數

class Node:   #宣告串列結構
    def __init__(self,val):
        self.val=val
        self.next=None

global indextable
indextable=[Node]*INDEXBOX #宣告動態陣列

def create_table(val):      #建立雜湊表副程式
    global indextable
    newnode=Node(val)
    myhash=val%7              #雜湊函數除以7取餘數
   
    current=indextable[myhash]
    
    if current.next==None:
        indextable[myhash].next=newnode
    else:
        while current.next!=None:
            current=current.next
    current.next=newnode #將節點加在串列

def print_data(val):       #列印雜湊表副程式
    global indextable
    pos=0
    head=indextable[val].next  #起始指標
    print('   %2d：\t' %val,end='')   #索引位址
    while head!=None:
        print('[%2d]-' %head.val,end='')
        pos+=1
        if pos % 8==7:
            print('\t')
        head=head.next
    print()

def findnum(num):     #雜湊搜尋副程式
    i=0
    myhash =num%7
    ptr=indextable[myhash].next
    while ptr!=None:
        i+=1
        if ptr.val==num:
            return i
        else:
            ptr=ptr.next
    return 0



#主程式

data=[0]*MAXNUM
index=[0]*INDEXBOX


for i in range(INDEXBOX):  #清除雜湊表
    indextable[i]=Node(-1)

print('原始資料：')
for i in range(MAXNUM):
    data[i]=random.randint(1,30)   #亂數建立原始資料
    print('[%2d] ' %data[i],end='') #並列印出來
    if i%8==7:
        print()

for i in range(MAXNUM):
    create_table(data[i])  #建立雜湊表
print()

while True:
    num=int(input('請輸入搜尋資料(1-30)，結束請輸入-1：'))
    if num==-1:
        break
    i=findnum(num)
    if i==0:
        print('#####沒有找到 %d #####' %num)
    else:
        print('找到 %d，共找了 %d 次!' %(num,i))
    

print('\n雜湊表：')
for i in range(INDEXBOX):
    print_data(i)          #列印雜湊表
print()
