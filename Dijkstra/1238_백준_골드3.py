# 다익스트라, 골드 3, 40분 정도
# 요즘 그래프를 너무 안한 것 같아서 다익스트라를 풀어봤다.
# 잘 모르겠다. 다른 제출한 사람들이랑 그리 차이가 나지도 않는 것 같은데
# 내꺼는 실행 속도가 너무 느리다. (통과하긴 했다.)
# 그리고 다익스트라가 뭔지 정확히 모르겠다.
# 일단은 제일 가까운 노드를 방문하고, 그 노드로부터 시작하는 모든 엣지를
# 힙에 넣고, 그 노드는 방문하지 않는 방식으로 이해하고 있다.
from heapq import heappop, heappush
import sys
n,m,x=[int(x) for x in input().split()]
arr=[[] for _ in range(n)]
go=[0]*n
back=[0]*n


def find(a,b):
    heap=[]
    dis=[1000000000]*n
    dis[a]=0
    for i in range(len(arr[a])):
        heappush(heap,[arr[a][i][1],arr[a][i][0]])
    while heap:
        tmp=heappop(heap)
        if tmp[0]<dis[tmp[1]]:
            dis[tmp[1]]=tmp[0]
            if tmp[1]==b:
                break
            for i in range(len(arr[tmp[1]])):
                heappush(heap,[arr[tmp[1]][i][1]+dis[tmp[1]],arr[tmp[1]][i][0]])
    if b==-1:
        return dis
    return dis[b]


for i in range(m):
    tmp=[int(x) for x in sys.stdin.readline().split()]
    arr[tmp[0]-1].append([tmp[1]-1,tmp[2]])
for i in range(n):
    if i!=x-1: go[i]=find(i,x-1)
back=find(x-1,-1)
ans=0
for i in range(n):
    ans=max(ans,go[i]+back[i])
print(ans)
