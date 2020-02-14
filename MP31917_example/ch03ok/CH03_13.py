select=0
class student:
    def __init_(self):
        self.name=''
        self.Math=0
        self.Eng=0
        self.no=''
        self.rlink=None
        self.llink=None

head=student()
head.llink=None
head.rlink=None
ptr=head #設定存取指標開始位置
select=0
while True:
    select=int(input('(1)新增 (2)離開 =>'))
    if select==2:
        break;
    new_data=student()
    new_data.name=input('姓名: ')
    new_data.no=input('學號: ')
    new_data.Math=eval(input('數學成績: '))
    new_data.Eng=eval(input('英文成績: '))
    #輸入節點結構中的資料 
    ptr.rlink=new_data
    new_data.rlink = None #下一元素的next先設定為None
    new_data.llink=ptr #存取指標設定為新元素所在位置
    ptr=new_data

print('-----向右走訪所有節點-----') 
ptr = head.rlink    #設定存取指標從串列首的右指標欄所指節點開始
while ptr!=None:
    print('姓名：%s\t學號:%s\t數學成績:%d\t英文成績:%d'  \
           %(ptr.name,ptr.no,ptr.Math,ptr.Eng))
    if ptr.rlink==None:
        break
    ptr = ptr .rlink    #將ptr移往右邊下一元素
    
print('-----向左走訪所有節點-----')
while ptr != None:
    print('姓名：%s\t學號:%s\t數學成績:%d\t英文成績:%d'  \
           %(ptr.name,ptr.no,ptr.Math,ptr.Eng))
    if(ptr.llink==head):
        break
    ptr = ptr .llink
