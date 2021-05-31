# 골드 3, 10분 내외, 그리디 문제
# 그냥 저냥 직관적으로 풀고, 이러면 시간초과 나지 않을래나 했는데
# 바로 풀렸다. 확실히 그리디가 쉽긴 쉬운 것 같다.
from heapq import heappush, heappop
N= int(input())
arr=[]
max1=0
for i in range(N):
    tmp=[int(x) for x in input().split()]
    max1=max(max1,tmp[0])
    heappush(arr,tmp)
ans=[0]*max1
while arr:
    tmp = heappop(arr)
    min1=100000000
    ind=-1
    for j in range(0,tmp[0]):
        if ans[j]<min1:
            min1=ans[j]
            ind=j
    if ind!=-1:
        ans[ind]=tmp[1]


print(sum(ans))
