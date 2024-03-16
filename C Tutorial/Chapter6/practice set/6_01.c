#include<stdio.h>

int main()
{
    int a = 67;
    int *b = &a;
    printf("The address of a us %u\n", &a);    
    printf("The value of a us %u\n", *b);    
    return 0;
}
