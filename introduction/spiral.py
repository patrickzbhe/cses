n = int(input())
for _ in range(n):
    y,x = [int(n) for n in input().strip().split()]
    if x > y:
        if x % 2 == 1:
            print(x**2 - y + 1)
        else:
            print((x-1)**2 + y )
    elif x < y:
        if y % 2 == 0:
            print(y**2 - x + 1)
        else:
            print((y-1)**2 + x )
    else:
        print(x**2 - y + 1)
