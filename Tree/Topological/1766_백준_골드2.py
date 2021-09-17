# 골드 2, 위상정렬, 10분
# 위상정렬의 기본형 문제이다. 근데 왜 골드 2인지는 잘 모르겠다.
# 풀기 전에 오랫만의 위상정렬이라 구글링으로 개념 한번 보고 풀었는데
# 그래서 그런지 쉽게 풀었다.
import sys,heapq
n,m=[int(x) for x in sys.stdin.readline().split()]
arr=[[] for _ in range(n+1)]
arrC=[0]*(n+1)
heap=[]
ans=[]
for i in range(m):
    tmp=[int(x) for x in sys.stdin.readline().split()]
    arr[tmp[0]].append(tmp[1])
    arrC[tmp[1]]+=1
for i in range(1,n+1):
    if arrC[i]==0:
        heapq.heappush(heap,i)
while heap:
    t=heapq.heappop(heap)
    ans.append(t)
    for i in range(len(arr[t])):
        arrC[arr[t][i]]-=1
        if arrC[arr[t][i]]==0:
            heapq.heappush(heap,arr[t][i])
print(*ans)
