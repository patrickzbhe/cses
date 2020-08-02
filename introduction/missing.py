n = int(input())
vals = [int(x) for x in input().strip().split()]

k = [1]*n
for v in vals:
    k[v-1] -= 1
for i in range(n):
    if k[i] != 0:
        print(i+1)
    
