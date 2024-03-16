#include<stdio.h>
int sum(int a, int b); // Declaration of Function

int main(){
    int result;
    result = sum(3,15);
    printf("The sum of a and b is %d\n", result);
    return 0;
}
int sum(int a, int b){
    int c;
    c = a + b;
    return c;
}
