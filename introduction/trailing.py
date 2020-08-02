n = int(input())
total = 0
for i in range(1,17):
    
    total += n // (5 ** i)
print(total)
