#include<stdio.h>

int main()
{
    int i = 1, sum=0, n=19;

    while(i<=n){
        sum +=i;
        i++;
    }
    printf("The sum(1 to 10) is %d\n", sum);
    return 0;
}
