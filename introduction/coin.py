for _ in range(int(input())):
    a,b = [int(x) for x in input().strip().split()]

    diff = abs(a-b)
    new = max(a,b) - (2 * diff)
    if new % 3 == 0 and new > -1:
        print("YES")
    else:
        print("NO")
