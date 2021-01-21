# 문자열 뒤집기

data = input()

# 최소 횟수
# 0으로 바꾸는게 빠른 경우
# 1로 바꾸는게 빠른 경우
cnt0 = 0
cnt1 = 0


if data[0] == 1:
    cnt0 += 1
else:
    cnt1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0, cnt1))






