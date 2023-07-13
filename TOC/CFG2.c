//Simulate the CFG for the language L = a^nb^mc^n where n,m >= 0;
/*
    Production Rules
    S -> aSc | B | ε
    B -> bB | ε
*/
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
    char str[50];
    int ruleCase = 1;
    printf("Enter any strings \n");
    scanf("%s", str);
    int length = strlen(str);
    //Invalid if the strign doesn't start with a or b.
    if(str[0] != 'a' && str[0] != 'b'){
        printf("The Given String cannot be generated!! ");
        exit(0);
    }

    //invalid if no of a and c are not equal
    int count = 0;
    for(int j = 0; j<length; j++){
        if(str[j] == 'a')
        count++;
        if(str[j] == 'c')
        count--;
        //checking if the string contains other letter than a, b and c
        else if(str[j] != 'a' && str[j] != 'b' && str[j] != 'c')
        {
            printf("Invalid string -> Other than 'a', 'b', and 'c'");
            exit(0);
        }

    }
    if(count != 0){
        printf("The Given String cannot be generated because no of a and c are not equal !");
        exit(0);
    }
    
    int i = 0;
    int close = 0;
    while(str[i] != '\0'){
        switch(ruleCase){
            case 1 : {
                if(str[i] == 'a'){
                    printf(" S -> aSc \n");
                }
                else if(str[i] == 'c'){
                    printf(" S -> ε \n");
                    close = 1;
                }
                else if(str[i] == 'b'){
                    printf(" S -> B \n");
                    printf(" B -> bB \n");
                    ruleCase = 2;
                }
                    break;
            }
            
            case 2 : {
                if(str[i] == 'b'){
                    printf(" B -> bB \n");
                }
                else if(str[i] == 'c'){
                    printf(" B -> ε \n");
                    close = 1;
                }
                    break;
            }

            default : {
                printf("Wrong Input... \n");
                break;
            }
        }
        if(close == 1)
        break;
        i++;
    }
    return 0;
}