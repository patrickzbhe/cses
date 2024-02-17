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

lli dp[1001][100001];
lli prices[1001];
lli pages[1001];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    int m;
    cin >> n;
    cin >> m;
    for (int i = 0; i < n; i++) {
        cin >> prices[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> pages[i];
    }
   
    for (int i = n - 1; i > -1; i--) {
        for (int j = 1; j < m + 1; j++) {
            lli buy = (prices[i] > j) ? 0 : dp[i+1][j-prices[i]] + pages[i];
            dp[i][j] = max(dp[i + 1][j], buy);
        }
    }
   
    cout << dp[0][m];
    return 0;
}