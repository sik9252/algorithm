import sys
input=sys.stdin.readline
import heapq

N=int(input())
M=int(input())

# 필요한 변수들
INF = float('inf')
# 1번 노드부터 시작하므로 N+1
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
  start,end,cost=map(int,input().split())
  graph[start].append([cost, end])

A,B=map(int,input().split())

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, node = heapq.heappop(q)

    # 기존 최단거리보다 크다면 무시
    if distance[node] < dist:
      continue

    # 연결된 모든 노드 탐색
    for nextDist, nextNode in graph[node]:
      newDist = nextDist + dist

      # 기존 거리보다 작으면 갱신
      if distance[nextNode] > newDist:
        distance[nextNode] = newDist
        heapq.heappush(q, [newDist, nextNode])
        
dijkstra(A)
print(distance[B])