n = int(input())

movies = []

for i in range(n):
    movies.append([int(x) for x in input().strip().split()])

movies.sort(key = lambda x: x[1])

ans = 0
end = -1

for i,m in enumerate(movies):
    if m[0] >= end:
        ans += 1
        end = m[1]

print(ans)
