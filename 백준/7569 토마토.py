import sys
input=sys.stdin.readline
from collections import deque

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dh=[0,0,0,0,-1,1]

M,N,H=map(int, input().split())
tomato=[]

for _ in range(H):
  tomato.append([list(map(int, input().split())) for _ in range(N)])

def bfs(temp):
  global day
  q=deque(temp)

  while q:
    h,y,x=q.popleft()

    for i in range(6):
      nx=x+dx[i]
      ny=y+dy[i]
      nh=h+dh[i]

      if 0<=nx<M and 0<=ny<N and 0<=nh<H and tomato[nh][ny][nx]==0:
        q.append([nh,ny,nx])
        tomato[nh][ny][nx] = tomato[h][y][x] + 1

        if day < tomato[nh][ny][nx]:
          day = tomato[nh][ny][nx]-1

temp=[]
day=0

for h in range(H):
  for y in range(N):
    for x in range(M):
      if tomato[h][y][x] == 1:
        temp.append([h,y,x])

bfs(temp)

for h in range(H):
  for y in range(N):
    for x in range(M):
      if tomato[h][y][x]==0:
        print(-1)
        exit()
        
print(day)