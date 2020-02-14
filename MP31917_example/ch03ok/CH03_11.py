import sys
import random

class student:   #宣告串列結構
    def __init__(self):
        self.num=0
        self.score=0
        self.next=None
        
def create_link(data,num): #建立串列副程式
    for i in range(num):
        newnode=student()
        if not newnode:
            print('Error!! 記憶體配置失敗!!')
            sys.exit(0) 
        if i==0:  #建立串列首
            newnode.num=data[i][0]
            newnode.score=data[i][1]
            newnode.next=None
            head=newnode
            ptr=head
        else:  #建立串列其他節點
            newnode.num=data[i][0]
            newnode.score=data[i][1]
            newnode.next=None
            ptr.next=newnode
            ptr=newnode
        newnode.next=head
    return ptr    #回傳串列

def print_link(head): #列印串列副程式
    i=0
    ptr=head.next
    while True:
        print('[%2d-%3d] => ' %(ptr.num,ptr.score),end='\t')
        i=i+1
        if i>=3 : #每行列印三個元素
            print()
            i=0
        ptr=ptr.next
        if ptr==head.next:
            break

def concat(ptr1,ptr2): #連結串列副程式
    head=ptr1.next  #在ptr1及ptr2中，各找任意一個節點
    ptr1.next=ptr2.next  #把兩個節點的next對調即可
    ptr2.next=head
    return ptr2

data1=[[None] * 2 for row in range(6)]
data2=[[None] * 2 for row in range(6)]

for i in range(1,7):
    data1[i-1][0]=i*2-1
    data1[i-1][1]=random.randint(41,100)
    data2[i-1][0]=i*2
    data2[i-1][1]=random.randint(41,100)
	
ptr1=create_link(data1,6)   #建立串列1
ptr2=create_link(data2,6)   #建立串列2
i=0
print('\n原 始 串 列 資 料：')
print('座號 成績   \t座號 成績   \t座號 成績')
print('==========================================')
print('   串列 1 ：')
print_link(ptr1)
print('   串列 2 ：')
print_link(ptr2)
print('==========================================')
print('連結後串列：')
ptr=concat(ptr1,ptr2)    #連結串列
print_link(ptr)
