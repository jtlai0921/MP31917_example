NONZERO=0
temp=1
Sparse=[[15,0,0,22,0,-15],[0,11,3,0,0,0],
        [0,0,0,-6,0,0],[0,0,0,0,0,0],
        [91,0,0,0,0,0],[0,0,28,0,0,0]] #宣告稀疏矩陣,稀疏矩陣的所有元素設為0
Compress=[[None] * 3 for row in range(9)] #宣告壓縮矩陣
	
print('[稀疏矩陣的各個元素]') #印出稀疏矩陣的各個元素
for i in range(6):
    for j in range(6):
        print('[%d]' %Sparse[i][j], end='\t')
        if Sparse[i][j] !=0:
            NONZERO=NONZERO+1
    print()

#開始壓縮稀疏矩陣
Compress[0][0] = 6
Compress[0][1] = 6
Compress[0][2] = NONZERO

for i in range(6):
    for j in range(6):
        if Sparse[i][j] !=0:
            Compress[temp][0]=i
            Compress[temp][1]=j
            Compress[temp][2]=Sparse[i][j]
            temp=temp+1
	
print('[稀疏矩陣壓縮後的內容]') #印出壓縮矩陣的各個元素
for i in range(NONZERO+1):
    for j in range(3):
        print('[%d] ' %Compress[i][j], end='')
    print()
