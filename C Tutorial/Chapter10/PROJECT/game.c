#include<stdio.h>
#include<sdkddkver.h>
#include<time.h>
int rockpaperscissor(char me, char comp){
    // Returns 1 if i win 0 if draw and -1 if comp wins
    // Draw condition
    if(me == comp){
        return 0;
    }
    // Non Draw Conditions
    if(me == 's' && comp == 'p'){
        return 1;
    }
    else if(me == 's' && comp == 'r'){
        return -1;
    }
    if(me == 'p' && comp == 'r'){
        return 1;
    }
    else if(me == 'p' && comp == 's'){
        return -1;
    }
    if(me == 'r' && comp == 's'){
        return 1;
    }
    else if(me == 'r' && comp == 'p'){
        return -1;
    }
}
int main(){
    char me, comp;
    int number = rand()%10 +1;
    if (number < 3){
        comp = 's';
    }
    else if(number>3 && number<6){
        comp = 'r';
    }
    else{
        comp = 'p';
    }
    printf("Enter 'r' for rock, 'p' for paper and 's' for scissor\n");
    scanf("%c", &me);
    int result = rockpaperscissor(me,comp);
    printf("You choose %c and Computer choose %c\n", me, comp);
    if(result == 0){
        printf("The game is drawn\n");
    }
    else if(result==1){
        printf("You win!!\n");
    }
    else{
        printf("You lose");
    }
    return 0;
}