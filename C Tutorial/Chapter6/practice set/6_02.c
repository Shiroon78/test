#include<stdio.h>

void printAdd(int a){
    printf("The value of a is %u\n", &a);
}
int main(int argc, char const *argv[])
{
    int i =  4;
    printf("The value of i is %d\n", i);
    printAdd(i);
    printf("The value of i is %u\n", &i);
    return 0;
}
