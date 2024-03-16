#include<stdio.h>

int main(){
    FILE *aptr;
    int numer = 45;
    aptr = fopen("generated,txt","w");
    fprintf(aptr, "The number is %d\n", numer);
    fprintf(aptr, "The number is %d\n", numer);
    fclose(aptr);
    return 0;
}