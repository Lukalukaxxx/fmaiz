#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n, m, maxn, r[100005], ans[100005];

int find(int pos)
{
	return r[pos]==pos?pos:r[pos] = find(r[pos]);
}

void add(int pos, int num)
{
	int _pos = find(pos);
	ans[_pos] = num;
	maxn = max(maxn, _pos);
	r[_pos] = find(_pos+1);
}

int main()
{
	scanf ("%d", &n);
	while(n)
	{
		maxn = -1;
		memset(ans, 0, sizeof ans);
		for(int i = 0; i <= 100000; i++) r[i] = i;
		for(int i = 1; i <= n; i++)
		{
			scanf("%d", &m);
			add(m, i);
		}
		printf("%d\n", maxn);
		for(int i = 1; i <= maxn; i++)
			printf("%d ", ans[i]);
		putchar('\n');
		scanf("%d", &n);
	}
	return 0;	
}
