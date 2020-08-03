import bisect
n = int(input())

blocks = [int(x) for x in input().strip().split()]

bases = []
    
bases.append(blocks[0])

for i,b in enumerate(blocks):
    if i == 0:
        continue
    if b >= bases[-1]:
        bases.append(b)
    else:
        k = bisect.bisect_right(bases,b)
        bases[k] = b
print(len(bases))


