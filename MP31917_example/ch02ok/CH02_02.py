N=2
#宣告2x2陣列arr並將所有元素指定為None
arr=[[None] * N for row in range(N)] 
print('|a1 b1|')
print('|a2 b2|')
arr[0][0]=input('請輸入a1:')
arr[0][1]=input('請輸入b1:')
arr[1][0]=input('請輸入a2:')
arr[1][1]=input('請輸入b2:')
#求二階行列式的值
result = int(arr[0][0])*int(arr[1][1])-int(arr[0][1])*int(arr[1][0]) 
print('|%d %d|' %(int(arr[0][0]),int(arr[0][1])))
print('|%d %d|' %(int(arr[1][0]),int(arr[1][1])))
print('行列式值=%d' %result)
