#include<stdio.h>
#include<string.h>
struct Employee{
    int code;
    float salary;
    char name[20];
};

void show(struct Employee emp){
    printf("The code of emplyee is  %d\n", emp.code);
    printf("The salary of emplyee is  %f\n", emp.salary);
    printf("The name of emplyee is  %d\n", emp.name);
}

int main(){
    struct Employee e1;
    struct Employee *ptr;
    ptr = &e1;
    ptr->code = 101;
    ptr->salary =  14.5;
    strcpy(ptr->name, "Rabi");
    show(e1);
    printf("The code of e1 is %d", e1.code);
    return 0;
}