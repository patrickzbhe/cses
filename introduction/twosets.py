n = int(input())

if n < 2:
    print("NO")
elif n % 2 == 1 and (n//2) % 2 == 1:
    print("YES")
    print(n//2)
    print(n," ".join(["{0} {1}".format(x,n-x) for x in range(1,1+((n-1)//2)//2)]))
    print(n//2 + 1)
    print(" ".join(["{0} {1}".format(x,n-x) for x in range(1+((n-1)//2)//2,n//2 + 1)]))
elif n % 2 == 0 and (n//2) % 2 == 0:
    print("YES")
    print(n//2)
    print(" ".join(["{0} {1}".format(x,n-x+1) for x in range(1,((n)//2)//2+1)]))
    print(n//2 )
    print(" ".join(["{0} {1}".format(x,n-x+1) for x in range(((n)//2)//2+1,n//2 + 1)]))
else:
    print("NO")
