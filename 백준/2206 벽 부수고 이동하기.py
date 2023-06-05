import sys
input=sys.stdin.readline
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,isBroken):
  q=deque()
  q.append([x,y,isBroken])

  while q:
    x,y,isBroken=q.popleft()

    # 출구에 도달하면 이동거리 출력
    if x==N-1 and y==M-1:
      return visited[x][y][isBroken]
    
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<N and 0<=ny<M:
        # 다음 이동할 곳이 벽이고 isBroken==False인 경우
        if isBroken==0 and maps[nx][ny]==1:
          visited[nx][ny][1]=visited[x][y][0]+1
          q.append([nx,ny,1])
        # 다음 이동할 곳이 벽이 아니고, 아직 방문 안한곳인 경우
        elif maps[nx][ny]==0 and visited[nx][ny][isBroken]==0:
          visited[nx][ny][isBroken]=visited[x][y][isBroken]+1
          q.append([nx,ny,isBroken])

  return -1
        

N,M=map(int, input().split())
maps=[list(map(int, input().rstrip())) for _ in range(N)]
visited=[[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0]=1

print(bfs(0,0,0))