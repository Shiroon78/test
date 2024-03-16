// Arrays to function
#include<stdio.h>

void printArray(int ptr[], int i){
    for (int a=0; a<i; a++){
        printf("The value of element %d is %d\n", a+1, ptr[a]);
    }
    ptr[2] = 5555; // This will directly manipulate the 3rd index value of the array in the memory
    
}
int main(){
    int arr[]= {1,2,3,4,5,6,7,8,9,0};
    printArray(arr, 10);
    printf("%d", arr[2]);
    return 0;
}
