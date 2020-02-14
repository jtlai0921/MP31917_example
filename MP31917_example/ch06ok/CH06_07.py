# =============== Program Description ===============                             
# 程式目的： 以鏈結串列實作二元運算樹
# ===================================================
#節點類別的宣告

class TreeNode:  #二元樹的節點宣告
    def __init__(self,value):
        self.value=value #節點資料
        self.left_Node=None #指向左子樹
        self.right_Node=None #指向左右子樹

#二元搜尋樹類別宣告
class Binary_Search_Tree:
    #建立空的二元搜尋樹
    def __init__(self):
        self.rootNode=None

    #利用傳入一個陣列的參數來建立二元樹
    def __init__(self,data):
        for i in range(len(data)):
            self.Add_Node_To_Tree(data[i])

    #將指定的值加入到二元樹中適當的節點
    def Add_Node_To_Tree(self,value):
        currentNode=self.rootNode
        if self.rootNode==None:  #建立樹根
            self.rootNode=TreeNode(value)
            return
        #建立二元樹
        while True:
            #符合這個判斷表示此節點在左子樹
            if value<currentNode.value:
                if currentNode.left_Node==None:
                    currentNode.left_Node=TreeNode(value)
                    return
                else:
                    currentNode=currentNode.left_Node
            #符合這個判斷表示此節點在右子樹
            else:
                if currentNode.right_Node==None:
                    currentNode.right_Node=TreeNode(value)
                    return
                else:
                    currentNode=currentNode.right_Node
                       
class Expression_Tree (Binary_Search_Tree):
    #初始化
    def __init__(self,information,index):
        #create方法可以將二元樹的陣列表示法轉換成鏈結表示法
        self.rootNode=self.create(information, index)

    # create方法的程式內容
    def create(self,sequence,index):
        if index >= len(sequence):   # 作為遞迴呼叫的出口條件
            return None
        else:
            tempNode = TreeNode((ord)(sequence[index]))
            # 建立左子樹
            tempNode.left_Node = self.create(sequence, 2*index)
            # 建立右子樹
            tempNode.right_Node =self.create(sequence, 2*index+1)
            return tempNode
        
    # preOrder(前序走訪)方法的程式內容
    def preOrder(self,node):
        if node != None:
            print((chr)(node.value),end='')
            self.preOrder(node.left_Node)
            self.preOrder(node.right_Node)
            
    # inOrder(中序走訪)方法的程式內容
    def inOrder(self,node):
        if node != None:
            self.inOrder(node.left_Node)
            print((chr)(node.value),end='')
            self.inOrder(node.right_Node)

    # postOrder(後序走訪)方法的程式內容
    def postOrder(self,node):
        if node != None:
            self.postOrder(node.left_Node)
            self.postOrder(node.right_Node)
            print((chr)(node.value),end='')
        
    # 判斷運算式如何運算的方法宣告內容
    def condition(self,oprator, num1, num2):
        if oprator=='*' :
            return ( num1 * num2 ) #乘法請回傳num1 * num2
        elif oprator=='/' :
            return ( num1 / num2 ) #除法請回傳num1 / num2
        elif oprator=='+' :
            return ( num1 + num2 ) #加法請回傳num1 + num2
        elif oprator=='-' :
            return ( num1 - num2 ) #減法請回傳num1 - num2
        elif oprator=='%' :
            return ( num1 % num2 ) #取餘數法請回傳num1 % num2
        else:
            return -1
        
    #傳入根節點,用來計算此二元運算樹的值
    def answer(self,node):
        firstnumber = 0
        secondnumber = 0
        #遞迴呼叫的出口條件
        if node.left_Node == None and node.right_Node == None :
            #將節點的值轉換成數值後傳回
            return node.value-48
        else:
            firstnumber = self.answer(node.left_Node)#計算左子樹運算式的值
            secondnumber = self.answer(node.right_Node) #計算右子樹運算式的值
            return self.condition((chr)(node.value), firstnumber, secondnumber)

#主程式

# 第一筆運算式
information1 = [' ','+','*','%','6','3','9','5' ]

# 第二筆運算式 
information2 = [' ','+','+','+','*','%','/','*',  \
                '1','2','3','2','6','3','2','2' ]

exp1 = Expression_Tree(information1, 1)
print('====二元運算樹數值運算範例 1: ====')
print('=================================')
print('===轉換成中序運算式===:  ',end='')
exp1.inOrder(exp1.rootNode)     
print('\n===轉換成前序運算式===:  ',end='')
exp1.preOrder(exp1.rootNode)    
print('\n===轉換成後序運算式===:  ',end='')
exp1.postOrder(exp1.rootNode)   

# 計算二元樹運算式的運算結果
print('\n此二元運算樹,經過計算後所得到的結果值: ',end='')
print(exp1.answer(exp1.rootNode))


# 建立第二棵二元搜尋樹物件
exp2 = Expression_Tree(information2, 1)
print()
print('====二元運算樹數值運算範例 2: ====')
print('=================================')
print('===轉換成中序運算式===:  ',end='')
exp2.inOrder(exp2.rootNode)     
print('\n===轉換成前序運算式===:  ',end='')
exp2.preOrder(exp2.rootNode)    
print('\n===轉換成後序運算式===:  ',end='')
exp2.postOrder(exp2.rootNode)   

# 計算二元樹運算式的運算結果
print('\n此二元運算樹,經過計算後所得到的結果值: ',end='')
print(exp2.answer(exp2.rootNode))

