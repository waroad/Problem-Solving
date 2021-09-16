# 골드 3, 그리디, 10분
# 일단은 쉬운 것부터.
# 이제부터 다시 시작해야겠다. 최대한 1일 1깃을 목표로 달려야겠다.
# 근래들어 너무 공부를 안했던 것 같다.

from operator import itemgetter
import heapq
n=int(input())

arr=[[int(x) for x in input().split()] for _ in range(n)]
arr.sort(key=itemgetter(0),reverse=True)
arr.sort(key=itemgetter(1))
cnt=0
heap=[]
for i in range(n):
    if arr[i][1]>cnt:
        heapq.heappush(heap,arr[i][0])
        cnt+=1
    else:
        tmp=heapq.heappop(heap)
        heapq.heappush(heap,max(tmp,arr[i][0]))

print(sum(heap))
