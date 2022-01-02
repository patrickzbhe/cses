n,m = [int(x) for x in input().strip().split()]
prices = [int(x) for x in input().strip().split()]
pages = [int(x) for x in input().strip().split()]

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n-1,-1,-1):
    for j in range(1,m + 1):
        buy = 0 if prices[i] > j else dp[i+1][j-prices[i]] + pages[i]
        dp[i][j] = max(dp[i+1][j], buy)
#print(dp)
print(dp[0][m])