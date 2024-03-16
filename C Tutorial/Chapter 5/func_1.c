#include <stdio.h>
void goodmorning();
void goodAfternoon();
void goodnight();

int main(){
    goodmorning();
    return 0;
}
void goodmorning(){
    printf("Good Morning\n");
    goodAfternoon();
}
void goodAfternoon(){
    printf("Good afternoon\n");
    goodnight();
}
void goodnight(){
    printf("Good Night\n");
}