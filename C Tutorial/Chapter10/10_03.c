#include<stdio.h>

int main(){
    FILE *ptr;
    int num;
    int num2;
    ptr = fopen("A_File.txt", "r");
    if(ptr == NULL){
        printf("The file does not Exist.\n");
    }
    else{
        fscanf(ptr, "%d", &num);
        fscanf(ptr, "%d", &num2);    
        fclose(ptr);
        printf("The value of num is %d\n", num);
        printf("The value of num is %d\n", num2);
    }
    return 0;
}