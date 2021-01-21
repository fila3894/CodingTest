# 곱하기 혹은 더하기
S = input()

data = int(S[0])

for i in range(1, len(S)):
    num = int(S[i])
    if data == 0 or data == 1:
        data += num
    else:
        data *= num

print(data)
