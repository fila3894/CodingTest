array = [[0 for col in range(10)] for row in range(10)]

for i in range(len(array)):
    array[0][i] = 1
    array[9][i] = 1

for i in range(len(array)):
    array[i][0] = 1
    array[i][9] = 1

fx, fy = map(int, input().strip().split(' '))
array[fx][fy] = 2



for a in array:
    for b in range(len(array)):
        print(a[b], end="")
    print()