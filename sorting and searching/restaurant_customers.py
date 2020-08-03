n = int(input())

enter = []
leave = []

for i in range(n):
    a,b = [int(x) for x in input().strip().split()]
    enter.append(a)
    leave.append(b)
enter.sort()
leave.sort()

i1 = 0
i2 = 0
biggest = 0
customers = 0

while i1 != n and i2 != n:
    if i1 == n:
        break

    if enter[i1] < leave[i2]:
        customers += 1
        i1 +=1
    else:
        customers -= 1
        i2 += 1
    if customers >biggest:
        biggest = customers
print(biggest)
