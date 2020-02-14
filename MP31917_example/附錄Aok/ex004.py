month=int(input('請輸入月份: '))    
if 2<=month and month<=4:
    print('充滿生機的春天')    
elif 5<=month and month<=7:
    print('熱力四射的夏季')
elif month>=8 and month <=10:
    print('落葉繽紛的秋季')
elif month==1 or (month>=11 and month<=12):
    print('寒風刺骨的冬季')
else:
    print('很抱歉沒有這個月份!!!')
