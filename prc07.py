array = [[0 for col in range(19)] for row in range(19)]
n = int(input("행/열 몇개를 바꾸겠습니까?(0->1): \n"))

#흰돌로 바꿀 행/열 입력 1->0
for i in range(n):
    x, y = map(int, input().strip().split(' '))
    for k in range(len(array)):
        array[k][y] = 1
        for l in range(len(array)):        
            array[x][l] = 1

for a in array:
    for b in range(len(array)):
        print(a[b], end="")
    print()

# 검은돌로 바꿀 행/열 입력 0->1
n = int(input("행/열 몇개를 바꾸겠습니까?(1->0): \n"))
for j in range(n):
    x, y = map(int, input().strip().split(' '))
    for i in range(len(array)):
        if array[x][i] == 0:
            array[x][i] = 1
        else:
            array[x][i] = 0
    for i in range(len(array)):
        if array[i][y] == 0:
            array[i][y] = 1
        else:
            array[i][y] = 0

for a in array:
    for b in range(len(array)):
        print(a[b], end="")
    print()