class student:
    def __init__(self):
        self.name=''
        self.no=''
        self.next=None
          
head=student()  #新增串列開頭元素
ptr = head    #設定存取指標位置
ptr.next = None    #目前無下個元素
select=0
while select!=2:
    select=int(input('(1)新增 (2)離開 =>'))
    if select ==2:
        break
    ptr.name=input('姓名 :')
    ptr.no=input('學號 :')
    new_data=student() #新增下一元素
    ptr.next=new_data   #連接下一元素
    new_data.next = None  #下一元素的next先設定為None
    ptr = new_data  #存取指標設定為新元素所在位置

ptr.next = head  #設定存取指標從頭開始
print()
ptr=head

while True:
     print('姓名：%s\t學號:%s\n' %(ptr.name,ptr.no))
     ptr=ptr.next  #將head移往下一元素
     if ptr.next==head:
         break
print('---------------------------------------------------------')
