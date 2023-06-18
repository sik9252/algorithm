import sys
input=sys.stdin.readline

N=int(input())
answer=0

for _ in range(N):
  word=input().rstrip()
  stack=[]

  for i in range(len(word)):
    if stack and word[i]==stack[-1]:
      stack.pop()
    else:
      stack.append(word[i])

  if not stack:
    answer+=1

print(answer)