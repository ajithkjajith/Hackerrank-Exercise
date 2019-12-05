#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	int arr_rows=6;
	int arr_columns=6;
	int arr[6][6]=
{{1, 1, 1, 0, 0, 0},
{0, 1, 0, 0, 0, 0},
{1 ,1 ,1 ,0 ,0 ,0},
{0, 0, 2, 4, 4, 0},
{0 ,0, 0, 2, 0, 0},
{0 ,0, 1, 2, 4, 0}};
int maximum=INT_MIN;
for(int i=0;i<arr_rows-2;i++)
{
	for(int j=0;j<arr_columns-2;j++)
	{
int sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2];

if(sum>maximum)
{
	maximum=sum;
	}

}
}

printf("%d\n",maximum );
	return 0;
}