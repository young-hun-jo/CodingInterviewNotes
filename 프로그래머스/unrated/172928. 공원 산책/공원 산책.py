def check_rule(x, y, op, n, maps, move):
    w = len(maps[0])
    h = len(maps)
    for _ in range(int(n)):
        dx, dy = move[op]
        x += dx
        y += dy
        if (x >= h or x < 0) or (y >= w or y < 0):
            return False
        elif maps[x][y] == 'X':
            return False
    return True

def solution(park, routes):
    move = {'W': (0, -1), 'N': (-1, 0), 'E': (0, 1), 'S': (1,0)}
    w = len(park[0])
    h = len(park)
    # 1.max : 2500
    maps = [[0] * w for _ in range(h)]
    # 2.max: 2500
    for i in range(h):
        for j in range(w):
            loc = park[i][j]
            if loc == 'S':
                x, y = i, j # 시작 위치
            maps[i][j] = park[i][j]
    # 3.max: 50 x 9 = 450
    for route in routes:
        op, n = route.split(" ")
        # 규칙 지킬 경우에만 이동
        if check_rule(x, y, op, n, maps, move):
            for _ in range(int(n)):
                dx, dy = move[op]
                x = x + dx
                y = y + dy
        else:
            continue
    return [x, y]

            
            

            
        
        
            