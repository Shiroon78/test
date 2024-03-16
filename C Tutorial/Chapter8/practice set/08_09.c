#include<stdio.h>

int main(){
    char st1[34];
    char st2[34];
    char c;
    int i = 0;
    printf("Enter the value of first string\n");
    scanf("%s", st1);
    printf("Enter the value of second string\n");
    scanf("%c", &c);
    while (c!='\n'){
        fflush(stdin);
        scanf("%c", &c);
        printf("%c", c);
        st2[i] = c;
        i++;
    }
    st2[i] = '\0';
    printf("The value of st1 is %s", st1);
    printf("The value of st1 is %s\n", st2);

    return 0;
}