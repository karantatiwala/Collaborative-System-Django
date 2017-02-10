#include<stdio.h>
#include<stdlib.h>
//#include<conio.h>
//#include<process.h>
void read();
void write();
struct record
{
  char movie[30];
  int platinum;
  int gold;
  int silver;
 // float sal;
}s;
int main()
{
int ch;
//clrscr();
    while(1)
    {
        printf("\n1:Enter Movie Details");
        printf("\n2:Read Records");
        printf("\n3:Exit");
        printf("\nEnter Your choice search:- ");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:
            write();
            break;
            case 2:
            read();
            break;
            case 3:
            exit(1);
            default:
            printf("\n\tOption not Available\n");
            break;
        }
    }
//getch();
}
void write()
{
int i,n=0;
FILE *fp;
    fp=fopen("movies.dat","wb");
    if(fp==NULL)
    {
        printf("can't create file");
       // getch();
        exit(1);
    }
    printf("\n\tHow Many Records You Want to Enter:=");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        
        printf("\nEnter Movie Name := ");
        scanf("%s",s.movie);

		printf("\nEnter tickets in Platinum := ");
        scanf("%d",&s.platinum);

		printf("\nEnter tickets in Gold := ");
        scanf("%d",&s.gold);

		printf("\nEnter tickets in Silver := ");
        scanf("%d",&s.silver);

        //flushall();
        //printf("\nEnter the Salary:=");
       // scanf("%f",&s.sal);
        printf("\n*****************\n");
        fwrite(&s,sizeof(s),1,fp);
    }
fclose(fp);
}
void read()
{
FILE *fp;
    fp=fopen("movies.dat","rb");
    if(fp==NULL)
    {
        printf("can't read file");
        //getch();
        exit(1);
    }
        while(fread(&s,sizeof(s),1,fp)==1)
        {
            //printf("\nEmployee ID := %d",s.id);
            printf("\nMovie Name := %s",s.movie);
			printf("\nPlatinum Available: = %d",  s.platinum);
			printf("\nGold Available: = %d",  s.gold);
			printf("\nSilver Available: = %d",  s.silver);
            //flushall();
            //printf("\nSalary:= %f",s.sal);
            printf("\n********************\n");
        }
fclose(fp);
}
