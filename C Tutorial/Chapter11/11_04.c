#include <stdio.h>
#include<stdlib.h>

int main(){
    int *ptr, *ptr2;
    // printf("The size of int on my pc is %d\n", sizeof(int));
    ptr = (int *)malloc(6 * sizeof(int));
    for(int i=0;i<600;i++){
        ptr2 = (int *)malloc(6 * sizeof(int));
        printf("Enter the value of %d\n", i);
        scanf("%d", &ptr[i]);
        free(ptr2);
    }
    for(int i = 0;i<6;i++){
        printf("The value of %d is %d\n", i, ptr[i]);
    }
    // free(ptr);
    return 0;
}