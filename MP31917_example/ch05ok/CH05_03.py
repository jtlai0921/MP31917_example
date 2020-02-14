queue=[0]*5
front=rear=-1
val=0
while rear<5 and val!=-1:
    val=int(input('請輸入一個值以存入佇列，欲取出值請輸入0。(結束輸入-1)：'))
    if val==0:
        if front==rear:
            print('[佇列已經空了]')
            break
        front+=1
        if front==5:
            front=0
        print('取出佇列值 [%d]' %queue[front])
        queue[front]=0
    elif val!=-1 and rear<5:
        if rear+1==front or rear==4 and front<=0:
            print('[佇列已經滿了]')
            break
        rear+=1
        if rear==5:
            rear=0
        queue[rear]=val
        
print('佇列剩餘資料：')
if front==rear:
    print('佇列已空!!')
else:
    while front!=rear:
        front+=1
        if front==5:
            front=0
        print('[%d]' %queue[front],end='')
        queue[front]=0
print()
