// =============== Program Description ===============
// �{���W�١G CH06_04.java                               
// �{���ت��G �H�쵲��C��@�G���B���
// ===================================================
//�`�I���O���ŧi
class TreeNode {
       int value;
       TreeNode left_Node;
       TreeNode right_Node;
       // TreeNode�غc�l
       public TreeNode(int value) {
          this.value=value;
          this.left_Node=null;
          this.right_Node=null;
       }
    } 
//�G���j�M�����O�ŧi
class Binary_Search_Tree {
   public TreeNode rootNode; //�G���𪺮ڸ`�I
   //�غc�l:�إߪŪ��G���j�M��
   public Binary_Search_Tree() { rootNode=null; }
   //�غc�l:�Q�ζǤJ�@�Ӱ}�C���ѼƨӫإߤG����
   public Binary_Search_Tree(int[] data) {
      for(int i=0;i<data.length;i++) 
         Add_Node_To_Tree(data[i]);
   }
   //�N���w���ȥ[�J��G���𤤾A�����`�I
   void Add_Node_To_Tree(int value) {
      TreeNode currentNode=rootNode;
      if(rootNode==null) { //�إ߾��
         rootNode=new TreeNode(value);
         return;
      }
      //�إߤG����
      while(true) {
         if (value<currentNode.value) { //�ŦX�o�ӧP�_���ܦ��`�I�b���l��
            if(currentNode.left_Node==null) {
              currentNode.left_Node=new TreeNode(value);
              return;
            }
            else currentNode=currentNode.left_Node;
         }
         else { //�ŦX�o�ӧP�_���ܦ��`�I�b�k�l��
            if(currentNode.right_Node==null) {
              currentNode.right_Node=new TreeNode(value);
              return;
            }
            else currentNode=currentNode.right_Node;
         }
       }
   }
}

class Expression_Tree extends Binary_Search_Tree{
   // �غc�l
   public Expression_Tree(char[] information, int index) {
      // create��k�i�H�N�G���𪺰}�C���ܪk�ഫ���쵲���ܪk
      rootNode = create(information, index);
   }
   // create��k���{�����e
   public TreeNode create(char[] sequence,int index) {
      TreeNode tempNode;            
      if ( index >= sequence.length )   // �@�����j�I�s���X�f����
         return null;
      else  { 
         tempNode = new TreeNode((int)sequence[index]);
         // �إߥ��l��
         tempNode.left_Node = create(sequence, 2*index);
         // �إߥk�l��
         tempNode.right_Node = create(sequence, 2*index+1);
         return tempNode;
      }
   }
  // preOrder(�e�Ǩ��X)��k���{�����e
   public void preOrder(TreeNode node) {
      if ( node != null ) {
         System.out.print((char)node.value);
         preOrder(node.left_Node);  
         preOrder(node.right_Node); 
      }
   }
   // inOrder(���Ǩ��X)��k���{�����e
   public void inOrder(TreeNode node) {
      if ( node != null ) {
         inOrder(node.left_Node);  
         System.out.print((char)node.value);
         inOrder(node.right_Node); 
      }
   }
   // postOrder(��Ǩ��X)��k���{�����e
   public void postOrder(TreeNode node) {
      if ( node != null ) {
         postOrder(node.left_Node);  
         postOrder(node.right_Node); 
         System.out.print((char)node.value);
      }
   }
   // �P�_�B�⦡�p��B�⪺��k�ŧi���e
   public int condition(char oprator, int num1, int num2) {
      switch ( oprator ) {
         case '*': return ( num1 * num2 ); // ���k�Ц^��num1 * num2
         case '/': return ( num1 / num2 ); // ���k�Ц^��num1 / num2
         case '+': return ( num1 + num2 ); // �[�k�Ц^��num1 + num2
         case '-': return ( num1 - num2 ); // ��k�Ц^��num1 - num2
         case '%': return ( num1 % num2 ); // ���l�ƪk�Ц^��num1 % num2
      }
      return -1;
   }
   // �ǤJ�ڸ`�I,�Ψӭp�⦹�G���B��𪺭�
   public int answer(TreeNode node) {
      int firstnumber = 0;       
      int secondnumber = 0;      
      // ���j�I�s���X�f����
      if ( node.left_Node == null && node.right_Node == null )
        // �N�`�I�����ഫ���ƭȫ�Ǧ^
        return Character.getNumericValue((char)node.value);
      else {
        firstnumber = answer(node.left_Node);  // �p�⥪�l��B�⦡����
        secondnumber = answer(node.right_Node); // �p��k�l��B�⦡����
        return condition((char)node.value, firstnumber, secondnumber);
      }
   }
 }
public class CH06_04 {
   public static void main(String[] args) {
      // �N�G���B���H�}�C���覡�ӫŧi
      // �Ĥ@���B�⦡
      char[] information1 = {' ','+','*','%','6','3','9','5' };
      // �ĤG���B�⦡
      char[] information2 = {' ','+','+','+','*','%','/','*',
                            '1','2','3','2','6','3','2','2' };
      Expression_Tree exp1 = new Expression_Tree(information1, 1);
      System.out.println("====�G���B���ƭȹB��d�� 1: ====");
      System.out.println("=================================");
      System.out.print("===�ഫ�����ǹB�⦡===:  ");
      exp1.inOrder(exp1.rootNode);     
      System.out.print("\n===�ഫ���e�ǹB�⦡===:  ");
      exp1.preOrder(exp1.rootNode);    
      System.out.print("\n===�ഫ����ǹB�⦡===:  ");
      exp1.postOrder(exp1.rootNode);   
      // �p��G����B�⦡���B�⵲�G
      System.out.print("\n���G���B���,�g�L�p���ұo�쪺���G��: ");
      System.out.println(exp1.answer(exp1.rootNode));
      // �إ߲ĤG�ʤG���j�M�𪫥�
      Expression_Tree exp2 = new Expression_Tree(information2, 1);
      System.out.println();
      System.out.println("====�G���B���ƭȹB��d�� 2: ====");
      System.out.println("=================================");
      System.out.print("===�ഫ�����ǹB�⦡===:  ");
      exp2.inOrder(exp2.rootNode);     
      System.out.print("\n===�ഫ���e�ǹB�⦡===:  ");
      exp2.preOrder(exp2.rootNode);    
      System.out.print("\n===�ഫ����ǹB�⦡===:  ");
      exp2.postOrder(exp2.rootNode);   
      // �p��G����B�⦡���B�⵲�G
      System.out.print("\n���G���B���,�g�L�p���ұo�쪺���G��: ");
      System.out.println(exp2.answer(exp2.rootNode));
      
   }
}