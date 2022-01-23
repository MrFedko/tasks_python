# Спирально заполнить двумерный массив:

n = int(input())
spiral = [[None]* n for j in range(n)]
dx, dy = 1,0
x, y = 0,0
for i in range(1, int(n**2 + 1)):
    spiral[x][y] = i
    nx, ny = x + dx, y + dy
    if 0<=nx<n and 0<=ny<n and spiral[nx][ny] == None:
        x, y = nx, ny
    else:
        dx,dy = -dy,dx
        x,y = x+dx, y+dy
                 
for i in range(n):
    for j in range(n):
        print(spiral[j][i], end = ' ')
    print()