#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
int n=5;int r=4;
	int arr[10]={1,2,3,4,5};
	for(int i=0;i<5;i++)
	{
		printf("%d",arr[((r%n)+i)%n]);
	}
	// printf("%d\n",arr );
	return 0;
}