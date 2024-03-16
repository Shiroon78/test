#include<stdio.h>

void change(int a);
int main(int argc, char const *argv[])
{
    int b = 344;
    printf("The value  of b befre cange is %d\n", b);
    change(b);
    printf("The value  of b after cange is %d\n", b);
    
    return 0;
}
void change(int b){
    b = 77;
}
