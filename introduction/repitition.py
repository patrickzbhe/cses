dna = input()

longest = 1
curr = 0
last = ""
for c in dna:
    if c == last:
        curr += 1
        if curr > longest:
            longest = curr
    else:
        last = c
        curr = 1
print(longest)
