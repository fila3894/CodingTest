a = [[0 for col in range(20)] for row in range(20)]

n = int(input("놓는 횟수: \n"))
for k in range(n):
    #x = int(input("가로: "))
    #y = int(input("세로: "))
    x, y = map(int, input().strip().split(' '))
    a[x][y] = 1


for i in range(1,20):
    for j in range(1,20):
        print(a[i][j], end="")
    print()