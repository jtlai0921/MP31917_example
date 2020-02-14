MAX=20

def fib(n):
    if n==1 or n==0:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
def fib_search(data,SearchKey):
    global MAX
    index=2
    #費氏數列的搜尋
    while fib(index)<=MAX :
        index+=1
    index-=1
    # index >=2
    #起始的費氏數
    RootNode=fib(index)
    #上一個費氏數
    diff1=fib(index-1)
    #上二個費氏數即diff2=fib(index-2)
    diff2=RootNode-diff1
    RootNode-=1 #這列運算式是配合陣列的索引是從0開始儲存資料
    while True:
        if SearchKey==data[RootNode]:
            return RootNode
        else:
            if index==2:
                return MAX #沒有找到
            if SearchKey<data[RootNode]:
                RootNode=RootNode-diff2#左子樹的新費氏數
                temp=diff1
                diff1=diff2#上一個費氏數
                diff2=temp-diff2#上二個費氏數
                index=index-1
            else:
                if index==3:
                    return MAX
                RootNode=RootNode+diff2#右子樹的新費氏數
                diff1=diff1-diff2#上一個費氏數
                diff2=diff2-diff1#上二個費氏數
                index=index-2
                

data=[5,7,12,23,25,37,48,54,68,77, \
      91,99,102,110,118,120,130,135,136,150]
i=0
j=0
while True:
    val=int(input('請輸入搜尋鍵值(1-150)，輸入-1結束：'))
    if val==-1: #輸入值為-1就跳離迴圈
        break
    RootNode=fib_search(data,val)#利用費氏搜尋法找尋資料
    if RootNode==MAX:
        print('##### 沒有找到[%3d] #####' %val)
    else:
        print('在第 %2d個位置找到 [%3d]' %(RootNode+1,data[RootNode]))
   
print('資料內容：')
for i in range(2):
    for j in range(10):
        print('%3d-%-3d' %(i*10+j+1,data[i*10+j]),end='')
    print()
