class student:
    def __init__ (self):
        self.num=0
        self.name=''
        self.score=0
        self.next=None

print('請輸入 5 筆學生資料：')      
node=student()
if not node:
    print('[Error!!記憶體配置失敗!]')
    sys.exit(0)
node.num=eval(input('請輸入座號：'))
node.name=input('請輸入姓名：')
node.score=eval(input('請輸入成績：'))
ptr=node #保留串列首，以ptr為目前節點指標
for i in range(1,5):
    newnode=student() #建立新節點
    if not newnode:
        print('[Error!!記憶體配置失敗!')
        sys.exit(0)
    newnode.num=int(input('請輸入座號：'))
    newnode.name=input('請輸入姓名：')
    newnode.score=int(input('請輸入成績：'))
    newnode.next=None
    ptr.next=newnode #把新節點加在串列後面
    ptr=ptr.next  #讓ptr保持在串列的最後面

print('  學  生  成  績')
print(' 座號\t姓名\t成績\n=====================')
ptr=node    #讓ptr回到串列首
while ptr!=None:
    print('%3d\t%-s\t%3d' %(ptr.num,ptr.name,ptr.score))
    node=ptr
    ptr=ptr.next #ptr依序往後走訪串列
