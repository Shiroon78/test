#include<stdio.h>

int main()
{
    int i = 5;
    int *j;
    j = &i;
    printf("The  value of i is %u\n", *j);
    printf("The address of i is %u\n", j);
    return 0;
}
