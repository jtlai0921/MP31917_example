#用遞迴函數求 n階乘的值

def factorial(i):
    if i==0:
        return 1
    else:
        product = i * factorial(i-1) # sum=n*(n-1)!所以直接呼叫本身
        return product

n=int(input('請輸入階乘數:'))
for i in range(n+1):
    print('%d !值為 %3d' %(i,factorial(i)))
