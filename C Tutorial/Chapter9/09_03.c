#include<stdio.h>
#include<string.h>
struct Employee{
    int code;
    float salary;
    char name[20];
};
int main(){
    struct Employee facebook[100];
    facebook[0].code = 100;
    facebook[0].salary = 45.3;
    strcpy(facebook[0].name, "Rabi");
    printf("Done!\n");
    facebook[1].code = 10;
    facebook[1].salary = 145.3;
    strcpy(facebook[1].name, "My_Enemy");
    printf("Done!\n");
    facebook[2].code = 1000;
    facebook[2].salary = 45.6;
    strcpy(facebook[2].name, "Delulu_World");
    printf("Done!\n");
    return 0;
}