#include <stdio.h>

int main()
{
    char i = 34;
    char *ptr = &i;
    printf("The vslue of ptr is %u\n", ptr);
    ptr = ptr + 1; // || (ptr++;)
    printf("The vslue of ptr is %u\n", ptr);
    return 0;
}
