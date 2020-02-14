sum=0
number=1
while True:
    if number==0:
        break
    number=int(input('數字0為結束程式,請輸入數字: '))
    sum+=number
    print('目前累加的結果為: %d' %sum)
