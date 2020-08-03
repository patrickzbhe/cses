n = int(input())

vals = [int(x) for x in input().strip().split()]

biggest = float('-inf')
going = float('-inf')

for v in vals:
    if v > going + v:
        going = v
    else:
        going += v
    if going > biggest:
        biggest = going
print(biggest)
