#include<stdio.h>
int swap(int *a, int *b);
void wrong_swap(int a, int b);

int main()
{
    int x = 4, y = 6;
    printf("The value of x and y is %d and %d\n", x,y);
    // wrong_swap(x,y); // will not work because this function is call by value 
    swap(&x, &y); // will work because this function is call by reference
    printf("The value of x and y is %d and %d\n", x,y);
    return 0;
}
void wrong_swap(int a,int b){
    int temp;
    temp = a;
    a = b;
    b = temp;
}
int swap(int *a, int *b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
