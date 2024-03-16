#include<stdio.h>
#include<string.h>
struct Employee{
    int code;
    float salary;
    char name[20];
};
int main(){
    struct Employee e1;
    struct Employee *ptr;
    ptr = &e1;
    // (*ptr).code = 101;
    ptr->code = 1001; // ---> can also be written using arrow operator
    printf("%d", e1.code);
    return 0;
}