//binary tree 
#include<stdio.h>
#include<stdlib.h>
struct treenode{
	int data;
	struct treenode *left;
	struct treenode *right;
};
struct treenode *create(int data){
	struct treenode *newnode=(struct treenode*)malloc(sizeof(struct treenode));
	newnode->data=data;
	newnode->left=NULL;
	newnode->right=NULL;
	return newnode;
}
struct treenode *insert(struct treenode *root,int data){
	if(root==NULL){
		root=create(data);
	}
	else if(data<=root->data){
		root->left=insert(root->left,data);
	}
	else if(data>root->data){
		root->right=insert(root->right,data);
	}
	return root;
}
void transverse(struct treenode *root){
	if(root!=NULL){
		transverse(root->left);
		printf("%d\t",root->data);
		transverse(root->right);
	}
}
int main(){
	struct treenode *root=NULL;
	root=insert(root,12);
	root=insert(root,13);
	root=insert(root,14);
	root=insert(root,15);
	printf("\n In order to transverse \n");
	transverse(root);
	return 0;
}

