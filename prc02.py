n=int(input()) # 출석 번호를 부른 횟수(사람 명수)
m=list(input().split(' ')) #무작위로 부른 1~23 사이의 출석번호
a=list(0 for i in range(23))

for i in range(1,24):
    a[i-1]=m.count(str(i))

#빈도수 출력
for j in range(23):
    print(a[j],end=' ')
