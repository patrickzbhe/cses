input()

o = 0
t = 0
c = {}
play = []

for i,v in enumerate(input().strip().split()):
   
    if v in c:
        
        c[v] = i
        k = 0
        while play[k] != v:
            del c[play[k]]
            k += 1
            o -= 1
        play = play[k:]
        
        if play[0] == v:
            del play[0]
        play.append(v)
    else:
        c[v] = i
        play.append(v)
        o += 1
        t = max(o,t)
print(t)
