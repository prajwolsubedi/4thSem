#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
    char s[100];
    int i,c=0,d=0,e=0;
    printf("Enter the string: ");
    scanf("%s",s);
     
    if(s[0]=='\0')
    {
        printf("S->e");
    	exit(0);
    } 
    for(i=0;s[i]!='\0';i++)
    {
    	 
        if(s[i]=='a')
        {
            c++;
        }
        else if(s[i]=='b')
        {
            d++;
        }
        else if(s[i]=='c')
        {
            e++;
        }
         
        else{
        	printf("This string is not acceptable!");
        	exit(0);
		}
    }
    if (c!=e){
 		printf("This string is not acceptable!");
    	exit(0);
	}
	printf("\nThe string is derived from the grammar.\n");
    printf("The leftmost derivation is:\n");
	printf("S->ABC\n");
	for(i=c;i>0;i--){
		printf("A->aA\n");
	}
	printf("A->e\n");
	for(i=d;i>0;i--){
		printf("B->bB\n");
	}
	printf("B->e\n");
	for(i=e;i>
	0;i--){
		printf("C->cC\n");
	}
	printf("C->e\n");
   
    
     return 0;
}

