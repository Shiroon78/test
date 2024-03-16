#include<stdio.h>

int main()
{
    int reading;
    printf("Enter your reading");
    scanf("%d", &reading);


    switch (reading);
    {
    case 1:
        printf("Your reading is 1");
        break;
    case 2:
        printf("Your reading is 2");
        break;
    case 3:
        printf("Your reading is 3");
        break;
    case 4:
        printf("Your reading is 4");
        break;
    case 5:
        printf("Your reading is 5");
        break;
    default:
        printf("Invalit Syntax");
        break;
    }
    return 0;
}
