import string
alpha = string.ascii_uppercase
s = input()

c_arr = [0] * 26

for c in s:
    
    c_arr[alpha.index(c)] += 1

odds = 0

answer = ""

for v in range(26):
    if c_arr[v]%2 == 0:
        answer += alpha[v] * (c_arr[v]//2)

for v in range(26):
    if c_arr[v]%2 == 1:
        odds += 1
        if odds > 1:
            print("NO SOLUTION")
            break
        answer += alpha[v] * (c_arr[v]//2 + 1)

if odds == 1:
    answer += answer[:-1][::-1]
    print(answer)
else:
    answer += answer[::-1]
    print(answer)
