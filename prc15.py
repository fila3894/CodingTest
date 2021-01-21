# 럭키 스트레이트

# 점수
n = input()

l = 0
for i in range(len(n)//2):
    l += int(n[i])

r = 0
for j in range(len(n)//2, len(n)):
    r += int(n[j])

if l == r:
    print("LUCKY")
else:
    print("READY")