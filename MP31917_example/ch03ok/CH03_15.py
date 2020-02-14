class employee:
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=''
        self.llink=None  #左指標欄
        self.rlink=None  #右指標欄

def findnode(head,num):
    ptr=head
    while ptr!=None:
        if ptr.num==num:
            return ptr
        ptr=ptr.rlink
    return ptr

def deletenode(head,del_node):
    if head==None: #雙向串列是空的
        print('[串列是空的]')
        return None
    if del_node==None:
        print('[錯誤:不是串列中的節點]')
        return None
    if del_node==head:
        head=head.rlink
        head.llink=None
    else:
        if del_node.rlink==None: #刪除串列尾
            del_node.llink.rlink=None
        else: #刪除中間節點
            del_node.llink.rlink=del_node.rlink
            del_node.rlink.llink=del_node.llink
    return head

llinknode=None
newnode=None
position=0
data=[[1001,32367],[1002,24388],[1003,27556],[1007,31299], \
      [1012,42660],[1014,25676],[1018,44145],[1043,52182], \
      [1031,32769],[1037,21100],[1041,32196],[1046,25776]]
namedata=['Allen','Scott','Mary','John','Mark','Ricky', \
          'Lisa','Jasica','Hanson','Amy','Bob','Jack']

print('員工編號 薪水 員工編號 薪水 員工編號 薪水 員工編號 薪水')
print('-------------------------------------------------------')

for i in range(3):
    for j in range(4):
        print('[%2d] [%3d]  ' %(data[j*3+i][0],data[j*3+i][1]),end='')
    print()

head=employee()  #建立串列首
if head==None:
    print('Error!! 記憶體配置失敗!!')
    sys.exit(0)
else:
    head.num=data[0][0]
    head.name=namedata[0]
    head.salary=data[0][1]
    llinknode=head
    for i in range(1,12):  #建立串列
        newnode=employee()
        newnode.num=data[i][0]
        newnode.name=namedata[i]
        newnode.salary=data[i][1]
        llinknode.rlink=newnode
        newnode.llink=llinknode
        llinknode=newnode

while True:
    position=int(input('\n請輸入要刪除的員工編號,要結束插入過程,請輸入-1：'))
    if position==-1: #迴圈中斷條件
        break
    else:
        ptr=findnode(head,position)
        head=deletenode(head,ptr)
		
print('\t員工編號    姓名\t薪水')
print('\t==============================')
ptr=head
while ptr!=None:
    print('\t[%2d]\t[ %-10s]\t[%3d]' %(ptr.num,ptr.name,ptr.salary))
    ptr=ptr.rlink
