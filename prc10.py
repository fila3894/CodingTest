# 모험가의 수
n = int(input())

# 공포도 입력
m = list(map(int, input().split(' ')))

# 오름차순 정렬
m.sort()

# 그룹의 수
g = 0
# 그룹의 포함된 모험가의 수
cnt = 0

# 공포도 낮은것 부터 비교
for i in m:
    cnt += 1
    if cnt >= i:
        g += 1
        cnt = 0

print(g)
