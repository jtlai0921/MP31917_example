class tree:
    def __init__(self):
        self.data=0
        self.left=None
        self.right=None
        
def inorder(ptr):      #中序走訪副程式
    if ptr!=None:
        inorder(ptr.left)
        print('[%2d] ' %ptr.data, end='')
        inorder(ptr.right)
        
def postorder(ptr):  #後序走訪
    if ptr!=None:
        postorder(ptr.left)
        postorder(ptr.right)
        print('[%2d] ' %ptr.data, end='')

def preorder(ptr):   #前序走訪
    if ptr!=None:
        print('[%2d] ' %ptr.data, end='')
        preorder(ptr.left)
        preorder(ptr.right)

def create_tree(root,val):  #建立二元樹函數
    newnode=tree()
    newnode.data=val
    newnode.left=None
    newnode.right=None
    if root==None:
        root=newnode
        return root
    else:
        current=root
        while current!=None:
            backup=current
            if current.data > val:
                current=current.left
            else:
                current=current.right
        if backup.data >val:
            backup.left=newnode
        else:
            backup.right=newnode
    return root
        
#主程式
data=[7,4,1,5,16,8,11,12,15,9,2]
ptr=None
root=None
for i in range(11):
    ptr=create_tree(ptr,data[i])       #建立二元樹
print('=======================================================')
print('中序式走訪結果：')
inorder(ptr)   #中序走訪
print()
print('=======================================================')
print('後序式走訪結果：')
postorder(ptr)   #中序走訪
print()
print('=======================================================')
print('前序式走訪結果：')
preorder(ptr)   #中序走訪
print()	
