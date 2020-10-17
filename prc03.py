n = int(input()) # 출석 번호를 부른 횟수(사람 명수)
m = list(input().split(' ')) #무작위로 부른 1~23 사이의 출석번호
a = []

for i in range(n):
    a.append(m[(n-1)-i])

for i in range(n):
    print(a[i], end=" ")

