# 볼링공 고르기(어려움)

# 볼링공 개수, 최대 무게
n, m = map(int, input().split(' '))
# 무게
k = list(map(int, input().split(' ')))

# 무게 담기 0이 담김
array = [0] * 11

# 무게당 해당하는 공 수 파악
for i in k:
    array[i] += 1
            
cnt = 0

for j in range(1, m + 1):
    n -= array[j]
    cnt += array[j] * n

print(cnt)
    
