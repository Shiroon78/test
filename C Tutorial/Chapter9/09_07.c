#include<stdio.h>
#include<string.h>
typedef struct Employee{
    int code;
    float salary;
    char name[20];
} emp;

void show(emp emp1){
    printf("The code of emplyee is  %d\n", emp1.code);
    printf("The salary of emplyee is  %f\n", emp1.salary);
    printf("The name of emplyee is  %d\n", emp1.name);
}
int main(){
    emp e1;
    emp *ptr;
    // Pointing ptr to e1
    ptr = &e1;
    ptr->code = 101;
    ptr->salary =  14.5;
    strcpy(ptr->name, "Rabi");
    show(e1);
    return 0;
}