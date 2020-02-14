import sys

class employee:
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=''
        self.next=None

def findnode(head,num):
    ptr=head
    while ptr.next!=head:
        if ptr.num==num:
            return ptr
        ptr=ptr.next
    ptr=None   
    return ptr

def deletenode(head,delnode):
    CurNode=employee()
    PreNode=employee()
    TailNode=employee()
    CurNode=None
    PreNode=None
    TailNode=None
    
    if head==None:
        print('[環狀串列已經空了]')
        return None
    else:
        if delnode==head: #要刪除的節點是串列首
            CurNode=head
            while CurNode.next!=head:
                CurNode=CurNode.next
                #找到最後一個節點並記錄下來
                TailNode=CurNode
                #(1)將串列首移到下一個節點
                head=head.next
                #(2)將串列最後一個節點的指標指向新的串列首
                TailNode.next=head
                return head
        else: #要刪除的節點不是串列首
            CurNode=head
            while CurNode.next!=delnode:
                CurNode=CurNode.next
            #(1)找到要刪除節點的前一個節點並記錄下來
            PreNode=CurNode
            #要刪除的節點
            CurNode=CurNode.next
            #(2)將要刪除節點的前一個指標指向要刪除節點的下一個節點
            PreNode.next=CurNode.next
            return head
      
position=0
namedata=['Allen','Scott','Marry','John', \
          'Mark','Ricky','Lisa','Jasica', \
          'Hanson','Amy','Bob','Jack']
data=[[1001,32367],[1002,24388],[1003,27556],[1007,31299], \
          [1012,42660],[1014,25676],[1018,44145],[1043,52182], \
          [1031,32769],[1037,21100],[1041,32196],[1046,25776]]
print('\n員工編號 薪水 員工編號 薪水 員工編號 薪水 員工編號 薪水')
print('-------------------------------------------------------')
for i in range(3):
    for j in range(4):
        print('[%2d] [%3d]  ' %(data[j*3+i][0],data[j*3+i][1]),end='')
    print()
head=employee() #建立串列首   
if not head:
    print('Error!! 串列首建立失敗!!')
    sys.exit(1)

head.num=data[0][0]
head.name=namedata[0]
head.salary=data[0][1]
head.next=None
ptr=head
for i in range(1,12):  #建立串列
    newnode=employee()
    newnode.num=data[i][0]
    newnode.name=namedata[i]
    newnode.salary=data[i][1]
    newnode.next=None
    ptr.next=newnode #將前一個節點指向新建立的節點
    ptr=newnode #新節點成為前一個節點
	
newnode.next=head #將最後一個節點指向頭節點就成了環狀鏈結
while True:
    position=int(input('請輸入要刪除的員工編號,要結束插入過程,請輸入-1：'))
    if position==-1:
        break #迴圈中斷條件
    else:
        ptr=findnode(head,position)
        if ptr==None:
            print('-----------------------')
            print('串列中沒這個節點....')
            break
        else:
            head=deletenode(head,ptr)
            print('已刪除第 %d 號員工 姓名：%s 薪資:%d' %(ptr.num,ptr.name,ptr.salary))
                
ptr=head #指向串列的開頭
print('\t員工編號    姓名\t薪水')
print('\t==============================')

while True:
    print('\t[%2d]\t[ %-10s]\t[%3d]' %(ptr.num,ptr.name,ptr.salary))
    ptr=ptr.next #指向下一個節點
    if head==ptr or head==head.next:
        break
