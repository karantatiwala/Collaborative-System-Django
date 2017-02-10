#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main( )
{
   char str1[ ] = "fresh" ;
   char str2[ ] = "refresh" ;
   int i, j, k ;
   i = strcmpi ( str1, "FRESH" ) ;
   j = strcmpi ( str1, str2 ) ;
   k = strcmpi ( str1, "f" ) ;
   printf ( "\n%d %d %d", i, j, k ) ;
   return 0;
}
