# 골드3, 플로이드 와샬, 30분
# 하지만 플로이드 와샬을 알아보지 않은 채로 그냥 dict를 사용해서 일단 풀었다.
# 곧 이 문제를 플로이드 와샬로 푼 파일을 하나 더 올릴 예정이다.
# dict가 정말 유용한 것 같긴하다. 어떤 값이 있는지 없는지
# BigO(1)로 찾을 수 있으니 말이다.

import sys,heapq
n,k=[int(x) for x in input().split()]
arr=[[] for _ in range(n+1)]
arrP=[{} for _ in range(n+1)]
arrC=[0]*(n+1)
for i in range(k):
    tmp=[int(x) for x in sys.stdin.readline().split()]
    arr[tmp[0]].append(tmp[1])
    arrC[tmp[1]]+=1
k=int(input())
heap=[]
for i in range(1,n+1):
    if arrC[i]==0:
        heapq.heappush(heap,i)
while heap:
    t = heapq.heappop(heap)
    for i in range(len(arr[t])):
        arrC[arr[t][i]] -= 1
        arrP[arr[t][i]][t]=1
        for j in (arrP[t]):
            if j in arrP[arr[t][i]]:
                continue
            arrP[arr[t][i]][j]=1

        if arrC[arr[t][i]] == 0:
            heapq.heappush(heap, arr[t][i])


for i in range(k):
    tmp = [int(x) for x in input().split()]
    if tmp[0] in arrP[tmp[1]]:
        print(-1)
    elif tmp[1] in arrP[tmp[0]]:
        print(1)
    else:
        print(0)
