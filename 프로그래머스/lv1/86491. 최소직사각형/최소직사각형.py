def solution(sizes):
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i])
    horizon = 0
    vertical = 0
    for i in range(len(sizes)):
        horizon = max(horizon, sizes[i][0])
        vertical = max(vertical, sizes[i][1])
    
    return horizon * vertical