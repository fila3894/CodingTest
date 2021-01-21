# 만들수 없는 최솟값

# 동전 개수
n = int(input())
# 화폐 단위(n개)
m = list(map(int, input().split(' ')))
# 오름차순으로 정렬
m.sort()

target = 1

for i in m:
    if target < i:
        break
    target += i

print(target)
