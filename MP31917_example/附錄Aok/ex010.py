#函數宣告
def fun(a,b):
    a,b=b,a
    print('函數內交换數值後:a=%d,\tb=%d\n' %(a,b))

a=10
b=15
print('呼叫函數前的數值:a=%d,\tb=%d\n'%(a,b))

print('\n-------------------------------------')
    
#呼叫函數
fun(a,b)
print('\n-------------------------------------')
print('呼叫函數後的數值:a=%d,\tb=%d\n'%(a,b))
