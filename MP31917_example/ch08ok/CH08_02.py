#[示範]:改良氣泡排序法
def showdata(data):    #利用迴圈列印資料
    for i in range(6):
        print('%3d' %data[i],end='')
    print()
    
def bubble (data):
    for i in range(5,-1,-1):
        flag=0 #flag用來判斷是否有執行交換的動作
        for j in range(i):
            if data[j+1]<data[j]:
                data[j],data[j+1]=data[j+1],data[j]
                flag+=1  #如果有執行過交換，則flag不為0
        if flag==0:
            break
        #當執行完一次掃描就判斷是否做過交換動作，如果沒有交換過資料
	#，表示此時陣列已完成排序，故可直接跳出迴圈   
        print('第 %d 次排序：' %(6-i),end='')
        for j in range(6):
            print('%3d' %data[j],end='')
        print()
    print('排序後結果為：',end='')
    showdata (data)

def main():
    data=[4,6,2,7,8,9]  #原始資料
    print('改良氣泡排序法原始資料為：')
    bubble (data)
    
main()
