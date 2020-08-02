n = int(input())
an = str(n)
while n != 1:
    an += " "
    if n%2 == 0:
        n //= 2
        an += str(n)
    else:
        n *= 3
        n += 1
        an += str(n)
print(an)
