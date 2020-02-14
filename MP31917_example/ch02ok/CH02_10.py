#將兩個最高次方相等的多項式相加後輸出結果
ITEMS=6
def PrintPoly(Poly,items):
    MaxExp=Poly[0]
    for i in range(1,Poly[0]+2):
        MaxExp=MaxExp-1
        if Poly[i]!=0:
            if (MaxExp+1)!=0:
                print(' %dX^%d ' %(Poly[i],MaxExp+1), end='')
            else:
                print(' %d' %Poly[i], end='')
            if MaxExp>=0:
                print('%c' %'+', end='')
    print()

def PolySum(Poly1, Poly2):
    result=[None]*ITEMS
    result[0] = Poly1[0]
    for i in range(1,Poly1[0]+2):
        result[i]=Poly1[i]+Poly2[i] #等羃的係數相加
    PrintPoly(result,ITEMS)

PolyA=[4,3,7,0,6,2]     #宣告多項式A
PolyB=[4,1,5,2,0,9]	#宣告多項式B
print('多項式A=> ', end='')
PrintPoly(PolyA,ITEMS)	#印出多項式A
print('多項式B=> ', end='')
PrintPoly(PolyB,ITEMS)	#印出多項式B
print('A+B => ', end='')
PolySum(PolyA,PolyB)	#多項式A+多項式B
