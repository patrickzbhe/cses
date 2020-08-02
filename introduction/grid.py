grid = [[False for i in range(7)] for j in range(7)]
visited = grid
answer = 0

path = input()

def move(r,c,steps):
    global answer
    #visited = [x[:] for x in visited]
    
    
    #printa(visited)

    if c == 0 and r == 6:
        if steps == 48:
            answer += 1
            return
        else:
            return
    #up
    if r >-1 and r < 6 and visited[r+1][c]:
        
        if r > 0:
            if visited[r-1][c]:
                if c < 6 and c > 0 and visited[r][c+1] == False and visited[r][c-1] == False:
                    return
        else:
            if c < 6 and c > 0 and visited[r][c+1] == False and visited[r][c-1] == False:
                return
      
    #down
    if r < 7 and r > 0 and visited[r-1][c]:
        if r < 6:
            if visited[r+1][c]:
                if c < 6 and c > 0 and visited[r][c+1] == False and visited[r][c-1] == False:
                    return
        else:
            if c < 6 and c > 0 and visited[r][c+1] == False and visited[r][c-1] == False:
                return
    #left
    if c > -1 and c < 6 and visited[r][c+1]:
        if c > 0:
            if visited[r][c-1]:
                if r < 6 and r > 0 and visited[r+1][c] == False and visited[r-1][c] == False:
                    return
        elif c == False:
            if r < 6 and r > 0 and visited[r+1][c] == False and visited[r-1][c] == False:
                return
       
    #right
    if c < 7 and c > 0 and visited[r][c-1]:
        if c < 6:
            if visited[r][c+1]:
                if r < 6 and r > 0 and visited[r+1][c] == False and visited[r-1][c] == False:
                    return
        elif c == 6:
            if r < 6 and r > 0 and visited[r+1][c] == False and visited[r-1][c] == False:
                return
    visited[r][c] = 1
    if path[steps] == "?":
        #up
        if r > 0 and visited[r-1][c] == False:
            move(r-1,c,steps + 1)
        #down
        if r < 6 and visited[r+1][c] == False:
            move(r+1,c,steps + 1)
        #left
        if c > 0 and visited[r][c-1] == False:
            move(r,c-1,steps + 1)
        #right
        if c < 6 and visited[r][c+1] == False:
            move(r,c+1,steps + 1)
    else:
        if path[steps] == "U" and r > 0 and visited[r-1][c] == False:
            move(r-1,c,steps + 1)
        if path[steps] == "D" and r < 6 and visited[r+1][c] == False:
            move(r+1,c,steps + 1)
        if path[steps] == "L" and c > 0 and visited[r][c-1] == False:
            move(r,c-1,steps + 1)
        if path[steps] == "R" and c < 6 and visited[r][c+1] == False:
            move(r,c+1,steps + 1)
    visited[r][c] = 0
move(0,0,0)
print(answer )
