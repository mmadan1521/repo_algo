#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>

typedef struct tnode {
   int data;
   struct tnode *lchild;
   struct tnode *rchild;
} tnode_t;

void print_tree_sideways(tnode_t *root, char *prefix)
{
   // implicit base case, return if root is NULL
   if (root) {
      strcat(prefix, "    ");
      print_tree_sideways(root->rchild, prefix);
      // inorder
      printf("%s %d\n", prefix, root->data);
      print_tree_sideways(root->lchild, prefix);
      prefix[strlen(prefix) - 4] = '\0';
   }
}


bool tree_remove_node(tnode_t **tree, int data)
{
   tnode_t *root = *tree;
   if (root) {
      if (data < root->data) { // check the left sub-tree
         if (tree_remove_node(&root->lchild, data)) { // pass address of lchild pointer
            return true;
         }
      } else if (data > root->data) { // check the right sub-tree
         if (tree_remove_node(&root->rchild, data)) { // pass address of rchild pointer
            return true;
         }
      } else { // found node
         tnode_t *del_node = root;
         printf("found node to be deleted: %d\n", del_node->data);
         if (root->rchild) {
            root = root->rchild;
            while (root->lchild != NULL) { // find the left most node
               root = root->lchild;
            }
            root->lchild = del_node->lchild; // attach deleted node's left subtree
         } else {
            root = root->lchild;
         }
         free(del_node); // free deleted node's memory
         *tree = root; // UPDATE THE TREE ROOT POINTER - basically updating the parent pointer
      }
   }
   return false;
}

bool tree_contains_node(tnode_t *root, int data)
{
   // implicit base case, return if root is NULL
   if (root) {
      if (data < root->data) {
         // check the left sub-tree
         if (tree_contains_node(root->lchild, data)) {
            return true;
         }
      } else if (data > root->data) {
         // check the right sub-tree
         if (tree_contains_node(root->rchild, data)) {
            return true;
         }
      } else {
         return true;
      }
   }
   return false;
}

void print_tree_preorder(tnode_t *root)
{
   // implicit base case, return if root is NULL
   if (root) {
      printf("%d ", root->data);
      print_tree_preorder(root->lchild);
      print_tree_preorder(root->rchild);
   }
}

void print_tree_inorder(tnode_t *root)
{
   // implicit base case, return if root is NULL
   if (root) {
      print_tree_inorder(root->lchild);
      printf("%d ", root->data);
      print_tree_inorder(root->rchild);
   }
}

void print_tree_postorder(tnode_t *root)
{
   // implicit base case, return if root is NULL
   if (root) {
      print_tree_postorder(root->lchild);
      print_tree_postorder(root->rchild);
      printf("%d ", root->data);
   }
}

void tree_add_node(tnode_t **tree, int data)
{
   tnode_t *root = *tree;

   printf("add node: %d\n", data);

   if (root == NULL) {
      tnode_t *node = malloc(sizeof(tnode_t));
      node->data = data;
      node->lchild = NULL;
      node->rchild = NULL;

      root = node;
      *tree = root; // UPDATE THE TREE ROOT POINTER - basically updating the parent pointer
   } else if (data < root->data) { // insert in the left subtree
      tree_add_node(&root->lchild, data); // pass address of lchild pointer
   } else if (data > root->data) { // insert in the right subtree
      tree_add_node(&root->rchild, data); // pass address of rchild pointer
   } else {
      // duplicate node - ignore for now
   }
}

int main()
{
   tnode_t *tree = NULL;
   char prefix[100];

   tree_add_node(&tree, 7);
   tree_add_node(&tree, 8);
   tree_add_node(&tree, 9);
   tree_add_node(&tree, 10);
   tree_add_node(&tree, 11);
   tree_add_node(&tree, 12);
   tree_add_node(&tree, 1);
   tree_add_node(&tree, 2);
   tree_add_node(&tree, 3);
   tree_add_node(&tree, 4);
   tree_add_node(&tree, 5);
   tree_add_node(&tree, 6);
   printf("\n");

   printf("tree contains node 8  : %s\n", tree_contains_node(tree, 8)? "Yes":"No");
   printf("tree contains node 2  : %s\n", tree_contains_node(tree, 2)? "Yes":"No");
   printf("tree contains node 12 : %s\n", tree_contains_node(tree, 12)? "Yes":"No");
   printf("tree contains node 6  : %s\n", tree_contains_node(tree, 6)? "Yes":"No");
   printf("tree contains node 7  : %s\n", tree_contains_node(tree, 7)? "Yes":"No");
   printf("tree contains node 0  : %s\n", tree_contains_node(tree, 0)? "Yes":"No");
   printf("tree contains node 20 : %s\n", tree_contains_node(tree, 20)? "Yes":"No");
   printf("\n");

   printf("print preorder: \n");
   print_tree_preorder(tree);
   printf("\n");

   printf("print inorder: \n");
   print_tree_inorder(tree);
   printf("\n");

   printf("print postorder: \n");
   print_tree_postorder(tree);
   printf("\n");

   printf("print tree sideways:\n");
   prefix[0] = '\0';
   print_tree_sideways(tree, prefix);
   printf("\n");

   tree_remove_node(&tree, 8);
   prefix[0] = '\0';
   print_tree_sideways(tree, prefix);
   printf("\n");

   tree_remove_node(&tree, 1);
   prefix[0] = '\0';
   print_tree_sideways(tree, prefix);
   printf("\n");

   tree_remove_node(&tree, 12);
   prefix[0] = '\0';
   print_tree_sideways(tree, prefix);
   printf("\n");

   tree_remove_node(&tree, 6);
   prefix[0] = '\0';
   print_tree_sideways(tree, prefix);
   printf("\n");

   tree_remove_node(&tree, 7);
   prefix[0] = '\0';
   print_tree_sideways(tree, prefix);
   printf("\n");
}
