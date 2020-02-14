import sys

#宣告字串陣列並初始化
newspaper=['1.水果日報','2.聯合日報','3.自由報', \
                          '4.中國日報','5.不需要']
#字串陣列的輸出
for i in range(5):
    print('%s  ' %newspaper[i], end='')

try :
    choice=int(input('請輸入選擇:'))
    #輸入的判斷
    if choice>=0 and choice<4:
        print('%s' %newspaper[choice-1])
        print('謝謝您的訂購!!!')
    elif choice==5:
        print('感謝您的參考!!!')
    else:
        print('數字選項輸入錯誤')

except ValueError:
    print('所輸入的不是數字')
