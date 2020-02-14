class employee:
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=''
        self.next=None
        
def findnode(head, num):
    ptr=head
    while ptr.next !=head:
        if ptr.num==num:
            return ptr
        ptr=ptr.next
    return ptr
    
def insertnode(head,after,num,salary,name):
    InsertNode=employee()
    CurNode=None
    InsertNode.num=num
    InsertNode.salary=salary
    InsertNode.name=name
    InsertNode.next=None
    if InsertNode==None:
        print('記憶體配置失敗')
        return None
    else:
        if head==None: #串列是空的
            head=InsertNode
            InsertNode.next=head
            return head
        else:
            if after.next==head: #新增節點於串列首的位置
                #(1)將新增節點的指標指向串列首
                InsertNode.next=head
                CurNode=head
                while CurNode.next!=head:
                    CurNode=CurNode.next
                #(2)找到串列尾後將它的指標指向新增節點
                CurNode.next=InsertNode
                #(3)將串列首指向新增節點
                head=InsertNode
                return head
            else: #新增節點於串列首以外的地方
                #(1)將新增節點的指標指向after的下一個節點
                InsertNode.next=after.next
                #(2)將節點after的指標指向新增節點
                after.next=InsertNode
                return head
     
position=0
namedata=['Allen','Scott','Marry','John','Mark','Ricky', \
          'Lisa','Jasica','Hanson','Amy','Bob','Jack']
data=[[1001,32367],[1002,24388],[1003,27556],[1007,31299], \
    [1012,42660],[1014,25676],[1018,44145],[1043,52182], \
    [1031,32769],[1037,21100],[1041,32196],[1046,25776]]

print('員工編號 薪水 員工編號 薪水 員工編號 薪水 員工編號 薪水')
print('-------------------------------------------------------')
for i in range(3):
    for j in range(4):
        print('[%2d] [%3d]  ' %(data[j*3+i][0],data[j*3+i][1]),end='')
    print()

head=employee() #建立串列首
if not head:
    print('Error!! 記憶體配置失敗!!')
    sys.exit(0)

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
    
newnode.next=head#將最後一個節點指向頭節點就成了環狀鏈結

while True:
    print('請輸入要插入其後的員工編號,如輸入的編號不在此串列中,')
    position=int(input('新輸入的員工節點將視為此串列的第一個節點,要結束插入過程,請輸入-1：'))
    if position == -1:  #迴圈中斷條件
        break
    else:
        ptr=findnode(head,position)
        new_num=int(input('請輸入新插入的員工編號：'))
        new_salary=int(input('請輸入新插入的員工薪水：'))
        new_name=input('請輸入新插入的員工姓名：')
        head=insertnode(head,ptr,new_num,new_salary,new_name)
                 
ptr=head #指向串列的開頭
print('\t員工編號    姓名\t薪水')         
print('\t==============================')

while True:
    print('\t[%2d]\t[ %-10s]\t[%3d]' %(ptr.num,ptr.name,ptr.salary))
    ptr=ptr.next#指向下一個節點
    if head ==ptr or head==head.next:
        break
	
