# 골드4, 그리디, 10분
# 그냥 오늘은 문제풀기 싫어서 쉬운거 풀었다.
# 더 할 말도 없다.

import sys,heapq
n=int(input())
arr=[]
for i in range(n):
    heapq.heappush(arr,int(sys.stdin.readline()))
ans=0
while len(arr)>1:
    a=heapq.heappop(arr)
    b=heapq.heappop(arr)
    ans+=a+b
    heapq.heappush(arr,a+b)

print(ans)
