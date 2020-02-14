#宣告三維陣列
num=[[[33,45,67],[23,71,66],[55,38,66]], \
     [[21,9,15],[38,69,18],[90,101,89]]]
value=num[0][0][0]#設定main為num陣列的第一個元素
for i in range(2):
    for j in range(3):
        for k in range(3):
            if(value>=num[i][j][k]):
                value=num[i][j][k] #利用三層迴圈找出最小值   
print("最小值= %d" %value)
