# 골드 3, 그래프, DFS, 30분 정도
# 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 찾는 문제이다.
# 어떻게 하면 구할까 하다가, 트리의 어느 점을 루트로 두어도 트리가
# 망가지지 않는 점을 이용해 우선 1번을 루트로 두고 1번에서 제일 거리가
# 먼 노드를 DFS로 찾은 뒤, 그 노드에서 거리가 제일 먼 노드를 찾기 위해
# 한번 더 DFS를 돌려서 구했다. 
# 내가 그래프, 최단거리, 트리에 약한 것 같아서 당분간은 그래프 문제를
# 풀어볼까 한다.

import sys
n=int(input())
arr=[[] for _ in range(n+1)]
for i in range(n):
    tmp=[int(x) for x in sys.stdin.readline().split()]
    for j in range(1,len(tmp)-1,2):
        arr[tmp[0]].append([tmp[j],tmp[j+1]])

ans=0
maxL=0
maxI=-1
arr1=[0]*(n+1)


def dfs(a):
    global ans,maxL,maxI
    arr1[a]=1
    if ans>maxL:
        maxL=ans
        maxI=a
    for i in range(len(arr[a])):
        if arr1[arr[a][i][0]]==1:
            continue
        ans+=arr[a][i][1]
        dfs(arr[a][i][0])
        ans-=arr[a][i][1]


dfs(3)
ans=0
maxL=0
arr1=[0]*(n+1)
dfs(maxI)
print(maxL)
