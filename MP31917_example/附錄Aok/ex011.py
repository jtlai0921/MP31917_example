def change(data):
    data[0],data[1]=data[1],data[0]
    print('函數內交換位置後：')
    for i in range(2):
        print('data[%d]=%3d' %(i,data[i]),end='\t')

#主程式
data=[16,25]
print('原始資料為：')
for i in range(2):
    print('data[%d]=%3d' %(i,data[i]),end='\t')
print('\n-------------------------------------')
change(data)
print('\n-------------------------------------')
print("排序後資料：")
for i in range(2):
    print('data[%d]=%3d' %(i,data[i]),end='\t')
