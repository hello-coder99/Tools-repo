//insertion sort algorithm 
#include<stdio.h>
#include<stdlib.h>
void display(int arr[],int size){
	int i;
	for(i=0;i<size;i++){
		printf("%d\t",arr[i]);
	}
	return;
}
int main(){
	int size;
	printf("Enter the size :");
	scanf("%d",&size);
	int arr[size];
	int i;
	for(i=0;i<size;i++){
		printf("Enter the element:");
		scanf("%d",&arr[i]);
	}
	printf("\n for insertion sort \n");
	int j;int temp;
	for(i=1;i<size;i++){
		for(j=0;j<i;j++){
			if(arr[j]>arr[i]){
				temp=arr[j];
				arr[j]=arr[i];
				arr[i]=temp;
			}
		}
	}
	printf("lets see it \n");
	display(arr,size);


	return 0;
}


