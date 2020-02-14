import sys

class student:
    def __init__(self):
        self.name=''
        self.Math=0
        self.Eng=0
        self.no=''
        self.next=None
        
head=student() #建立串列首
head.next=None
ptr = head
Msum=Esum=num=student_no=0
select=0

while select !=2:
    print('(1)新增 (2)離開 =>')
    try:
        select=int(input('請輸入一個選項: '))
    except ValueError:
         print('輸入錯誤')
         print('請重新輸入\n')
    if select ==1:
        new_data=student() #新增下一元素
        new_data.name=input('姓名:')
        new_data.no=input('學號:')
        new_data.Math=eval(input('數學成績:'))
        new_data.Eng=eval(input('英文成績:'))
        ptr.next=new_data #存取指標設定為新元素所在位置
        new_data.next=None #下一元素的next先設定為None
        ptr=ptr.next
        num=num+1

ptr=head.next #設定存取指標從頭開始
print()
while ptr !=None:
    print('姓名：%s\t學號:%s\t數學成績:%d\t英文成績:%d' \
           %(ptr.name,ptr.no,ptr.Math,ptr.Eng))
    Msum=Msum+ptr.Math
    Esum=Esum+ptr.Eng
    student_no=student_no+1
    ptr=ptr.next #將ptr移往下一元素

if student_no !=0:
    print('---------------------------------------------------------')
    print('本串列學生數學平均成績:%.2f 英文平均成績:%.2f' \
      %(Msum/student_no,Esum/student_no))
