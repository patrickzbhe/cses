n,x = [int(x) for x in input().strip().split()]

vals = [int(x) for x in input().strip().split()]

c = {}

for i,v in enumerate(vals):
    if v in c:
        
        c[v].append(i+1)
    else:
        c[v] = [i+1]

for v in vals:
    if x-v in c:
        if x-v == v:
            if len(c[v]) > 1:
                print(c[x-v][0],c[v][-1])
        else:
            print(c[x-v][0],c[v][0])
            break
        
else:
    print("IMPOSSIBLE")
