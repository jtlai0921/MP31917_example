class list_node:
    def __init__(self):
        self.val=0
        self.next=None

head=[list_node()]*9 #宣告一個節點型態陣列
        
run=[0]*9

def dfs(current): #深度優先函數
    run[current]=1
    print('[%d] ' %current, end='')
    ptr=head[current].next
    while ptr!=None:
        if run[ptr.val]==0: #如果頂點尚未走訪，
            dfs(ptr.val)           #就進行dfs的遞迴呼叫
        ptr=ptr.next
        
#圖形邊線陣列宣告       
data=[[1,2],[2,1],[1,3],[3,1], \
      [2,4],[4,2],[2,5],[5,2], \
      [3,6],[6,3],[3,7],[7,3], \
      [4,8],[8,4],[5,8],[8,5], \
      [6,8],[8,6],[8,7],[7,8]]
for i in range(1,9):  #共有八個頂點
    run[i]=0        #設定所有頂點成尚未走訪過
    head[i]=list_node()
    head[i].val=i   #設定各個串列首的初值
    head[i].next=None
    ptr=head[i]        #設定指標為串列首
    for j in range(20): #二十條邊線
        if data[j][0]==i: #如果起點和串列首相等，則把頂點加入串列
            newnode=list_node()
            newnode.val=data[j][1]
            newnode.next=None
            while True:
                ptr.next=newnode    #加入新節點
                ptr=ptr.next
                if ptr.next==None:
                    break
        

print('圖形的鄰接串列內容：')      #列印圖形的鄰接串列內容
for i in range(1,9):
    ptr=head[i]
    print('頂點 %d=> ' %i,end='')
    ptr =ptr.next
    while ptr!=None:
        print('[%d] ' %ptr.val,end='')
        ptr=ptr.next
    print()
print('深度優先走訪頂點：')      #列印深度優先走訪的頂點
dfs(1)
print()
 
