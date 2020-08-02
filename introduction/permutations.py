n = int(input())
if n == 1:
    print("1")
elif n < 4:
    print("NO SOLUTION")
else:
    print(" ".join(str(n) for n in range(2,n + 1,2)) + " " +  " ".join(str(n) for n in range(1,n + 1,2)))
    
