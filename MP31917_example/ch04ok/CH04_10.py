MAX=50
infix_q=['']*MAX

#運算子優先權的比較，若輸入運算子小於堆疊中運算子
#，則傳回值為1，否則為0                          

#在中序表示法佇列及暫存堆疊中，運算子的優先順序表，
#其優先權值為INDEX/2  
def compare(stack_o, infix_o):
    infix_priority=['']*9
    stack_priority=['']*8
    index_s=index_i=0
    infix_priority[0]='q'; infix_priority[1]=')'
    infix_priority[2]='+'; infix_priority[3]='-'
    infix_priority[4]='*'; infix_priority[5]='/'
    infix_priority[6]='^'; infix_priority[7]=' '
    infix_priority[8]='('
    
    stack_priority[0]='q'; stack_priority[1]='('
    stack_priority[2]='+'; stack_priority[3]='-'
    stack_priority[4]='*'; stack_priority[5]='/'
    stack_priority[6]='^'; stack_priority[7]=' '
    
    while stack_priority[index_s] != stack_o:
        index_s+=1

    while infix_priority[index_i] != infix_o:
        index_i+=1

    if int(index_s/2) >= int(index_i/2):
        return 1
    else:
        return 0
	
def infix_to_postfix():
    global MAX
    global infix_q
    rear=0; top=0; i=0
    #flag=0
    index = -1
    stack_t=['']*MAX  #以堆疊儲存還不必輸出的運算子

    str_=str(input('請開始輸入中序運算式: '))

    while i <len(str_):
        index+=1
        infix_q[index]=str_[i]
        i+=1

    infix_q[index+1]='q' #以q符號作為佇列的結束符號
    
    print('後序表示法 : ', end='')
    stack_t[top]='q'  #於堆疊最底端加入q為結束符號

    for flag in range(index+2):
        if infix_q[flag]==')': #輸入為)，則輸出堆疊內運算子，直到堆疊內為(
            while stack_t[top]!='(':
                print('%c' %stack_t[top],end='')
                top-=1
            top-=1
            #break
            #輸入為q，則將堆疊內還未輸出的運算子輸出
        elif infix_q[flag]=='q':
            while stack_t[top]!='q':
                print('%c' %stack_t[top],end='')
                top -=1
            #break
            #輸入為運算子，若小於TOP在堆疊中所指運算子，
            #則將堆疊所指運算子輸出，若大於等於TOP在堆疊
            #中所指運算子，則將輸入之運算子放入堆疊
        elif infix_q[flag]=='(' or infix_q[flag]=='^' or \
             infix_q[flag]=='*' or infix_q[flag]=='/' or \
             infix_q[flag]=='+' or infix_q[flag]=='-' :
            
            while compare(stack_t[top], infix_q[flag])==1:
                print('%c' %stack_t[top], end='')
                top-=1
            top+=1
            stack_t[top] = infix_q[flag]
            #break
            #輸入為運算元，則直接輸出
        else:
            print('%c' %infix_q[flag],end='')
            #break

#主程式
print('------------------------------------------')
print('中序運算式轉成後序運算式')
print('可以使用的運算子包括:^,*,+,-,/,(,)等 ')
print('------------------------------------------')

infix_to_postfix()
