# 정렬 문제
# 국영수

# 학생 수
n = int(input())

# 학생 정보 받을 리스트
students = []

for _ in range(n):
    students.append(input().split())

# 오름차순 + // 내림차순 - 배열의 위치기준
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 학생 리스트에서 이름만 출력

for i in students:
    print(i[0])

