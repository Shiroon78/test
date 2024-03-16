#include<stdio.h>
#include<string.h>
struct Employee{
    int code;
    float salary;
    char name[10];
};
int main(){
    struct Employee e1, e2, e3;
    printf("Enter the value of code.\n");
    scanf("%d", &e1.code);
    printf("Enter the value of salary.\n");
    scanf("%f", &e1.salary);
    printf("Enter the value of name.\n");
    scanf("%s", e1.name);
    printf("Enter the value of code.\n");
    scanf("%d", &e2.code);
    printf("Enter the value of salary.\n");
    scanf("%f", &e2.salary);
    printf("Enter the value of name.\n");
    scanf("%s", e2.name);
    printf("Enter the value of code.\n");
    scanf("%d", &e3.code);
    printf("Enter the value of salary.\n");
    scanf("%f", &e3.salary);
    printf("Enter the value of name.\n");
    scanf("%s", e3.name);
    return 0;
}