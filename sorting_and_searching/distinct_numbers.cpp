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

bool vals[1200000000];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ifstream inFile;
    inFile.open("test_input.txt");
    lli n;
    lli t;
    lli dist = 0;

    cin >> n;

    set<int> s;

    for (int i = 0; i < n; i++)
    {
        cin >> t;

        s.insert(t);
    }

    cout << s.size();
    return 0;
}