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

    int n;

    cin >> n;
    int k;

    for (int i = 1; i < n + 1; i++)
    {

        vector<int> s;
        int i2 = i;
        while (i2 > 0)
        {
            s.push_back(i2 % 10);
            i2 = i2 / 10;
        }

        dp[i] = 1e6;
        for (int j = 0; j < s.size(); j++)
        {

            k = s.at(j);

            if (i - k >= 0)
            {

                dp[i] = min(dp[i - k] + 1, dp[i]);
            }
        }
    }

    cout << dp[n];
}