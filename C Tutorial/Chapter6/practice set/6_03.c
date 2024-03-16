#include<stdio.h>
void sumAvg(int a, int b, int *sum, float *avg){
    *sum =a + b;
    *avg = (float)*sum/2;
}
int main()
{
    int i,j,sum;
    float avg;
   
    i =3;
    j =4;
    sumAvg(i,j, &sum, &avg);
    printf("The value of sum is %d\n, The value of avg is  %f\n", sum, avg);
    return 0;
}
