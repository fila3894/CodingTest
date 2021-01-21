# 문자열 재정렬

# 문자, 숫자 입력
S = input()
# 결과(재정렬) 값
result = []
# 숫자 합
val = 0

for i in S:
    if i.isalpha():
        result.append(i)
    else:
        val += int(i)

result.sort()
if val != 0:
    result.append(str(val))

# 예제 형태로 출력(리스트를 문자열로 변환)
print(''.join(result))

