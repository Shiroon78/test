#include<stdio.h>

int main()
{
    int arr[10];
    // int *ptr = &arr[0];
    int *ptr;
    ptr = arr;
    ptr =  ptr+2;
    if (ptr == &arr[2]){
        printf("This points to the same address");
    }
    else{
        printf("This points to the same address");
    }
    return 0;
}
    
