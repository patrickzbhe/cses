#include <iostream>
#include <math.h>
#include <vector>
#include <string>
#include <bits/stdc++.h>
#include <algorithm>
#define lli long long int
#define li long int
#define ld long double
#include <fstream>
using namespace std;

lli dp[101][1000001];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    int x;
    cin >> n;
    cin >> x;

    int coins[n];

    for (int i = 0; i < n; i++)
    {
        cin >> coins[i];
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < x + 1; j++)
        {
            if (j == 0)
            {
                dp[i][j] = 1;
            }
            dp[i][j] += dp[i - 1][j];
            if (j >= i)
            {
                dp[i][j] = dp[i][i - j];
            }
        }
    }
    cout << dp[100][x];
}