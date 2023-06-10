import sys
input=sys.stdin.readline

N=int(input())
files={}

for _ in range(N):
  file=input().rstrip().split(".")[1]
  if file not in files:
    files[file]=1
  else:
    files[file]+=1

for key,value in dict(sorted(files.items())).items():
  print(key, value)