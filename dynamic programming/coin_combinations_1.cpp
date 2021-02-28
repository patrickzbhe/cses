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

lli dp[1000001];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    int x;
    cin >> n;
    cin >> x;
    dp[0] = 1;
    int coins[n];

    for (int i = 0; i < n; i++)
    {
        cin >> coins[i];
    }

    for (int i = 1; i < x + 1; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i >= coins[j])
            {
                dp[i] += dp[i - coins[j]];
                dp[i] %= 1000000007;
            }
        }
    }
    cout << dp[x];
}