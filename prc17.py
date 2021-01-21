# 탐색 DFS/BFS
from collections import deque

# 너비우선탐색(BFS 사용) - 최단 거리찾기

# 도시 수, 도로 개수, 최단 거리 설정, 출발 도시
n, m, k, x = map(int, input().split(' '))
graph = [[] for _ in range(n + 1)]

# 도시 간 연결
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)

# 최단 거리 초기화
dist = [-1] * (n + 1)
dist[x] = 0
# BFS 수행
q = deque([x])

while q:
    now = q.popleft()
    # 이동 가능한 도시 확인
    for next_node in graph[now]:
        if dist[next_node] == -1:
            dist[next_node] = dist[now] + 1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)    

