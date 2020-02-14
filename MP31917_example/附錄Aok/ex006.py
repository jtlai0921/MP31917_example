sum=0
number=int(input('請輸入整數: '))
  
#遞增for迴圈,由小到大印出數字 
print('由小到大排列輸出數字:')
for i in range(1,number+1):
    sum+=i #設定sum為i的和 
    print('%d' %i,end='')
    #設定輸出連加的算式 
    if i<number:
        print('+',end='')
    else:
        print('=',end='')
print('%d' %sum)

sum=0
#遞減for迴圈,由大到小印出數字 
print('由大到小排列輸出數字:')
for i in range(number,0,-1):
    sum+=i 
    print('%d' %i,end='')
    if i<=1:
        print('=',end='')
    else:
        print('+',end='')
print('%d' %sum)
