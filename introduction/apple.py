n = int(input())

apples = [int(n) for n in input().strip().split()]

lowest = 123131231312323

half = sum(apples)/2

def search(i,s):
    global lowest
    diff = abs(half-s)
    if diff < lowest:
        lowest = diff

    if i < len(apples)-1:
        search(i + 1, s + apples[i])
        search(i + 1, s)

search(0,0)

print(int(lowest *2 ) )
    
