n,m,k = [int(x) for x in input().strip().split()]
apps = sorted([int(x) for x in input().strip().split()])
apts = sorted([int(x) for x in input().strip().split()])
i = 0
nice = 0
for c in apps:
    while i < len(apts) - 1 and c - apts[i] > k :
        i += 1
    if i < len(apts)  and abs(c-apts[i]) <= k:
      
        nice += 1
        i += 1
        
print(nice)
