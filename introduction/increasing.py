n = int(input())
arr = [int(x) for x in input().strip().split()]

low = 0
tot = 0
for e in arr:
    if e < low:
        tot += low - e
    else:
        low = e

print(tot)
