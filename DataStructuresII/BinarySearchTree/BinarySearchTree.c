#include "BinarySearchTree.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int add(TreeNode **root, void *element, TreeComparator f){


     //Quando a árvore/sub-árvore está vazia
     //ou alcançou o local da folha, atualiza o pai
     if(*root == NULL){
        TreeNode *newNode = (TreeNode*) malloc(sizeof(TreeNode));
        if(newNode == NULL)return 0;

         newNode->element = element;
         newNode->left = NULL;
         newNode->right = NULL;

         *root = newNode;
         return 1;
     }
     //left > right = 1
     //left < right = -1
     //left == right = 0
     int compValue = f(element,(*root)->element);

     if(compValue > 0){
         //avança para a direita
         return add(&(*root)->right,element,f);
     }
     else if(compValue < 0){
         //avança para a esquerda
         return add(&(*root)->left,element,f);
     }else{
         //não é possível replicar o mesmo valor
         return -1;
     }
}