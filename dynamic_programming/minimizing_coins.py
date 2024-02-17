n,x = [int(x) for x in input().strip().split()]
coins = [int(x) for x in input().strip().split()]

dp = [(10 ** 8 + 1)] * 1000001

dp[0] = 0


for i in range(1,x+1):
    
    for c in coins:
        if i - c >= 0:
            if dp[i-c] + 1 < dp[i]:
                if dp[i-c] != 10 ** 8 + 1:
                    dp[i] = dp[i-c] + 1
if dp[x] != 10 ** 8 + 1:
    print(dp[x])
else:
    print(-1)
