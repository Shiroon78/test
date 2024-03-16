#include<stdint.h>

int main(){
    char str1[45]= "Coding";
    char *str2= " is fun";
    strcat(str1, str2);
    printf("Final str is %s", str1);
    return 0;
}