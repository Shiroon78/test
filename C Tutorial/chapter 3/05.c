#include<stdio.h>


int main()
{
    int a;
    printf("Enter a\n");
    scanf("%d", &a);
// One Liner
    (a<5)? printf("a is less than 5") : printf("a is greater than 5");
    return 0;
}
