n = int(input())

print("0")

for i in range(1,n):
    if i == 1:
        print("6")
        last = 6
        continue
    if i == 2:
        print("28")
        total = 28
        continue
    
  
    additional = (i+1)**2 - (i**2)
    
    total += additional * (i**2)
    b = (i+1) * 2 - 2
    total += (b * (b+1)) // 2
    total -= 16
    total -= (i-3) * 8
    
    print(total)
