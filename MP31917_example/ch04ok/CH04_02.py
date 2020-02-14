import random
global top

top=-1
k=0

def push(stack,MAX,val):
    global top
    if top>=MAX-1:
        print('[堆疊已經滿了]')
    else:
        top=top+1
        stack[top]=val
        
def pop(stack):
    global top
    if top<0:
        print('[堆疊已經空了]')
    else:
        top=top-1
        return stack[top]

def shuffle(old):
    result=[]
    while old:
        p=random.randrange(0,len(old))
        result.append(old[p])
        old.pop(p)
    return result

card=[None]*52
card_new=[None]*52
stack=[0]*52
for i in range(52):
    card[i]=i+1

print('[洗牌中...請稍後!]')

card_new=shuffle(card)

i=0
while i!=52:
    push(stack,52,card_new[i])  #將52張牌推入堆疊
    i=i+1

print('[逆時針發牌]')
print('[顯示各家牌子] 東家\t  北家\t   西家\t    南家')
print('=================================')

while top>=0:
    #print(stack[top])
    style = (stack[top]) % 4	#計算牌子花色
    #print('style=', style)
    if style==0:  #梅花
        ascVal='club'
    elif style==1:  #方塊
        ascVal='diamond'
    elif style==2:   #紅心
        ascVal='heart'
    elif style==3:
        ascVal='spade'   #黑桃
    
    print('[%s%3d]\t' %(ascVal,stack[top]%13+1),end='')
    if top%4==0:
        print()
    top-=1
