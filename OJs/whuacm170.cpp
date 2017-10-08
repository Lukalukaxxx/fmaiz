#include <cstdio>
#include <algorithm>
using namespace std;

int n, a[1000005];

int main()
{
	scanf("%d", a);
	while(a[0])
	{
		a[++n] = a[0];
		scanf("%d", a);
	}
	sort(a+1, a+n+1);
	a[0] = 0;
	for(int i = 1; i <= n; i++)
	if(a[i] != a[i-1]) printf("%d ", a[i]);
	return 0;
}
