#include<stdio.h>

int main(){
    // char str[] = "SHIRO";
    char str[] = {'S','H','I','R','O','\0'};
    char *ptr = str;
    while (*ptr != '\0'){
        printf("%c", *ptr);
        ptr++;
    }
    
    return 0;
}
