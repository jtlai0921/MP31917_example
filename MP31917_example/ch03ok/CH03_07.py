class LinkedList:  #宣告串列結構
    def __init__(self):
        self.coef=0
        self.exp=0
        self.next=None
def create_link(data): #建立多項式副程式
    for i in range(4):
        newnode=LinkedList()
        if not newnode:
            print("Error!! 記憶體配置失敗!!")
            sys.exit(0)
        if i==0:
            newnode.coef=data[i]
            newnode.exp=3-i
            newnode.next=None
            head=newnode
            ptr=head
        elif data[i]!=0:
            newnode.coef=data[i]
            newnode.exp=3-i
            newnode.next=None
            ptr.next=newnode
            ptr=newnode
    return head

def print_link(head):  #列印多項式副程式
    while head !=None:
        if head.exp==1 and head.coef!=0:  #X^1時不顯示指數
            print("%dX + " %(head.coef), end='')
        elif head.exp!=0 and head.coef!=0:
            print("%dX^%d + " %(head.coef,head.exp), end='')
        elif head.coef!=0: #X^0時不顯示變數
            print("%d" %(head.coef))
        head=head.next
    print()
        
def sum_link(a,b): #多項式相加副程式
    i=0
    ptr=b
    plus=[None]*4
    while a!=None: #判斷多項式1
        if a.exp==b.exp: #指數相等，係數相加
            plus[i]=a.coef+b.coef
            a=a.next
            b=b.next
            i=i+1
        elif b.exp>a.exp: #B指數較大，指定係數給C
            plus[i]=b.coef
            b=b.next
            i=i+1
        elif a.exp>b.exp: #A指數較大，指定係數給C
            plus[i]=a.coef
            a=a.next
            i=i+1
    return create_link(plus)     #建立相加結果串列C

def main():
    data1=[3,0,4,2]         #多項式A的係數
    data2=[6,8,6,9]         #多項式B的係數
    #c=LinkedList()
    print("原始多項式：\nA=",end='')
    a=create_link(data1)    #建立多項式A
    b=create_link(data2)    #建立多項式B
    print_link(a)           #列印多項式A
    print("B=",end='')
    print_link(b)           #列印多項式B
    print("多項式相加結果：\nC=",end='') #C為A、B多項式相加結果
    print_link(sum_link(a,b))         #列印多項式C
    	
main()
