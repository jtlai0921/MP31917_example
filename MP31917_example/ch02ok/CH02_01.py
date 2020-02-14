Score=[87,66,90,65,70]
Total_Score=0
for count in range(5):
    print('第 %d 位學生的分數:%d' %(count+1,Score[count]))
    Total_Score+=Score[count]
print('-------------------------')
print('5位學生的總分:%d' %Total_Score)
