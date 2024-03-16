#include<stdio.h>

int main(){
    FILE *ptr;
    ptr = fopen("tetx.txt", "r"); //--> For reading a file
    // ptr = fopen("tetx.txt", "w"); //--> For writing a file

    return 0;
}