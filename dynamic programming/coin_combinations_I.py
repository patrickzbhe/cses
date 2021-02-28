n,x = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]

ways = [0] * 1000001
ways[0] = 1

for i in range(1,x+1):
    for c in coins:
        if i >= c:
            ways[i] += ways[i-c]
            ways[i] %= 10**9+7

print(ways[x])
