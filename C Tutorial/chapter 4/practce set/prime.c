#include <stdio.h>

int main(){
    int a, prime=1;
    printf("Enter the value of a\n");
    scanf("%d", &a);
    for (int i = 2; i < a; i++)
    {
        if (a % i == 0){
            prime = 0;
            break;
        }
    }
    if (prime == 0 && a!=2){
        printf("This is not a prime number");
    }
    else{
        printf("It is a prime number");
    }
    return 0;
}

