#include<stdio.h>

int main(){
    FILE *ptr;

    ptr = fopen("demo.txt", "w");
    fputc('c',ptr);
    fclose(ptr);
    return 0;
}