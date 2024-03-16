#include<stdio.h>

int main()
{
    int lenght, breadth;

    printf("What is the length of the rectangle?\n");
    scanf("%d", &lenght);
    printf("What is the breadth of the rectangle?\n");
    scanf("%d", &breadth);

    printf("The area of the rectangle is %d", lenght*breadth);
    return 0;
}
