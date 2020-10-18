w, h = map(int, input().strip().split(' '))
n = int(input())

array = [[0 for col in range(w)] for row in range(h)]


#d = 0(가로),1(세로)
for j in range(n):
    l, d, x, y = map(int, input().strip().split(' ')) 
    if d == 0:
        for i in range(y-1, y+l-1):
            array[x-1][i] = 1
    elif d == 1:
        for i in range(x-1, x+l-1):
            array[i][y-1] = 1
    else:
        print("잘못 입력하셨습니다(0,1 외의 값 입력)")
            

for a in array:
    for b in range(len(array)):
        print(a[b], end="")
    print()

