n = int(input()) # 출석 번호를 부른 횟수(사람 명수)
m = [int(x) for x in input().split(" ")] #무작위로 부른 1~23 사이의 출석번호

if n != 1:
    if m[0] <= m[1]:
        min = m[0]
    else:
        min = m[1]
    for i in range(2, n):
        if min <= m[i]:
            continue
        else:
            min = m[i]
else:
    min = m[0]
    
print(min)

