#include<stdio.h>
// Multi-dimensional Array
int main()
{
    int std = 3;
    int num_sub = 5;
    int marks[3][5];

    for (int i=0; i<std; i++){
        for (int j = 0; j < num_sub; j++){
            printf("Enter the marks of student %d in subject %d\n", i+1, j+1);
            scanf("%d", &marks[i][j]);
        }
    }
    for (int i=0; i<std; i++){
        for (int j = 0; j < num_sub; j++){
            printf("The marks of student %d in subject %d is %d\n", i+1, j+1, marks[i][j]);
        }
    }
    return 0;
}
    
        

