# 골드 3, 30분, 플로이드 와샬
# 이것도 상관관계가 있는지 없는지 판단하는 문제이다.
# 원래 플로이드 와샬이 이런쪽으로 많이 쓰이는 모양이다.
# 한번 쭉 문제를 본 다음에 이제 git 에만 올리고 로컬에는 저장 안하려고 한다.
import sys

n=int(input())
k=int(input())
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(k):
    tmp = [int(x) for x in sys.stdin.readline().split()]
    arr[tmp[0]][tmp[1]] = 1
    arr[tmp[1]][tmp[0]] = -1
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if arr[j][i]+arr[i][k]==2:
                arr[j][k]=1
                arr[k][j]=-1
for i in range(1,n+1):
    cnt=0
    for j in range(1,n+1):
        if arr[i][j]==0:
            cnt+=1
    print(cnt-1)
