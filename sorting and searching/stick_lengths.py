n = int(input())

vals = [int(x) for x in input().strip().split()]
vals.sort()
middle = vals[len(vals)//2]


o = 0

for v in vals:
    o += abs(middle - v)
print(o)
