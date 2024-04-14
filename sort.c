#include<stdio.h>
#include<stdlib.h>

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sort(int arr[], int size){
    int i, j, min;
    for(i = 0; i < size; i++){
        min = i;
        for(j = i + 1; j < size; j++){
            if(arr[j] < arr[min]){
                min = j;
            }
        }
        swap(&arr[i], &arr[min]);
    }
}

int main(){
    int arr[] = {5, 3, 9, 7, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    sort(arr, n);
    printf("SORTED\n");
    int i;
    for(i = 0; i < n; i++){
        printf("%d\n", arr[i]);
    }
    return 0;
}

