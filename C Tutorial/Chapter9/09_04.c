#include<stdio.h>
#include<string.h>
struct Employee{
    int code;
    float salary;
    char name[20];
};
int main(){
    struct Employee new_strct = {100, 14.5, "Shiro"};
    printf("Code = %d\n", new_strct.code);
    printf("Salary = %f\n", new_strct.salary);
    printf("Name = %s\n", new_strct.name);
    return 0;
}