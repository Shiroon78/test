#include <stdio.h>

void display(); // Function Prototype
int main(){
    int a;
    printf("This is Initializing display function\n");
    display();
    printf("Display function finished its work");
    return 0;
}

// Function Definition
void display(){
    printf("This is display\n");
}
