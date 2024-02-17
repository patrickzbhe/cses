n,x = [int(x) for x in input().strip().split()]
c = sorted([int(x) for x in input().strip().split()])

ans = 0

l = 0
r = n - 1

while r >= l:
    if c[l] + c[r] < x + 1:
        ans += 1
        l += 1
        r -= 1
    else:
        ans += 1
        r -= 1
print(ans)
    
