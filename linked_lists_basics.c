#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};
void insert_at_end(struct node **head){
    struct node *newnode=(struct node*)malloc(sizeof(struct node));
    printf("Enter the data :");
    scanf("%d",&newnode->data);
    if(*head==NULL){
        *head=newnode;
        return;
    }
    struct node *ptr=*head;
    while(ptr->next!=NULL){
        ptr=ptr->next;
    }
    ptr->next=newnode;
    newnode=ptr;
}
void insert_at_middle(struct node **head){
    struct node *newnode=(struct node*)malloc(sizeof(struct node));
    printf("Enter the data:");
    scanf("%d",&newnode->data);
    if(*head==NULL){
        *head=newnode;
        return;
    }int pos;
    printf("At which position do you want to enter the data :");
    scanf("%d",&pos);
    pos--;
    struct node *cptr=*head;
    struct node *temp=cptr->next;
    while(pos>0){
        cptr=cptr->next;
        temp=temp->next;
        pos--;
    }
    cptr->next=newnode;
    newnode->next=temp->next;
    free(temp);
}
void insert_at_begnning(struct node **head){
    struct node *newnode=(struct node*)malloc(sizeof(struct node));
    printf("Enter the data:");
    scanf("%d",&newnode->data);
    while(*head==NULL){
        *head=newnode;
        return;
    }
    struct node*ptr=*head;
    newnode->next=ptr;
    ptr=newnode;
    *head=ptr;
}
void display(struct node *ptr){
    while(ptr!=NULL){
        printf("%d\t",ptr->data);
        ptr=ptr->next;
    }
}
int main(){
    struct node *head=NULL;
    int num;
    while(1){
        printf("\n1:data at begin 2: at middle 3: at end 4: display 5:exit :");
        scanf("%d",&num);
        if(num==1){
            insert_at_begnning(&head);
        }
        else if(num==2){
            insert_at_middle(&head);
        }
        else if(num==3){
            insert_at_end(&head);
        }
        else if(num==4){
            display(head);
        }
        else if(num==5){
            break;
        }
        else{
            continue;
        }
    }
    return 0;
    
}
