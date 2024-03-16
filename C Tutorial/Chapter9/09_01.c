#include<stdio.h>
#include<string.h>
struct Employee{
    int code;
    float salary;
    char name[10];
};
int main(){
    struct Employee e1;
    e1.code = 100;
    e1.salary = 13.5;
    // e1.name = "Shiro"; --> This wnnt work
    strcpy(e1.name, "Shiro");
    printf("%d\n", e1.code);
    printf("%f\n", e1.salary);
    printf("%s\n", e1.name);

    return 0;
}