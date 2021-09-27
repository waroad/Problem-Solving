# 골드 4, 그리디, 1시간 좀 넘게
# 이거는 생각보다 너무 오래 걸렸다.
# 문제가 날짜를 가지고 하는건데, 끝나는 날짜가 다음 값의 시작하는 날짜랑 같을 경우,
# 1 적을 경우, 1 많을 경우들을 생각하는 것이 번거로웠다.
# 막상 정답인 논리를 생각하는데는 30분도 안걸렸지만, 그걸 구현하는데 너무 오래 걸렸다.

import sys
from operator import itemgetter
n=int(input())
arr=[]
tmpA=0
for i in range(n):  # 달 별로 계산하지는 않고, 각 달을 다 31일이 있다고 치환하였다. 문제를 푸는데는 문제가 없다.
    tmp=[int(x) for x in sys.stdin.readline().split()]
    a=(tmp[0]-1)*31+tmp[1]
    b=(tmp[2]-1)*31+tmp[3]-1
    if a<63:
        tmpA=max(tmpA,b)
        continue
    arr.append([a,b])
if tmpA:
    arr.append([63,tmpA])
arr.sort(key=itemgetter(1),reverse=True)
arr.sort(key=itemgetter(0))
ans1=arr[0][1]+1
ans2=0
flower=1
if arr[0][0] <= 63:  # 제일 이른 꽃이 3월 1일보다 먼저 필 경우
    for i in range(1,len(arr)):
        if ans1 >= 341:
            break
        if arr[i][0] <= ans1 <= arr[i][1]:
            if arr[i][0]>ans2:
                flower+=1
                ans2 = ans1
            ans1 = arr[i][1] + 1
        elif arr[i][0] > ans1:
            flower=0
            break
    if ans1<341:
        flower=0
else:
    flower=0
print(flower)
