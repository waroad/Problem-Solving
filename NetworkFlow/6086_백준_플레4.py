# 알고리즘 보고 이해하고 푸는데 1시간 반정도
# 요즘 프로젝트, 수업, 시험 때문에 바쁘기도하고, 카카오 코테가 끝나고나니 다시 코테는 시들시들해져서 안풀었다.
# 카카오 인턴쉽 1차는 통과해서 면접을 다음주에 보는데, 잘 됐으면 좋겠다.
# 학교 수업인 '고급문제해결' 에서 나온 과제가, 백준에 똑같은 것이 있어서 오랫만에 그냥 제출했다.
# 최대 유량 구하는 알고리즘을 처음 접해봤는데, 이런 알고리즘도 있구나 하고 확실히
# 기업 코테 수준을 넘어서면 알아야 하는 것이 많구나 하고 느꼈다.
# 사실 이거는 아직도 원리는 이해했는데, 코드는 백프로 이해는 아니다.

from collections import deque
graph=[[0 for _ in range(52)] for _ in range(52)]

ans=0
dict1={}
n=int(input())
cnt=0
for i in range(n):
    arr=[x for x in input().split()]
    if arr[0] not in dict1:
        dict1[arr[0]]=cnt
        cnt+=1
    if arr[1] not in dict1:
        dict1[arr[1]]=cnt
        cnt+=1
    graph[dict1[arr[0]]][dict1[arr[1]]]+=int(arr[2])
    graph[dict1[arr[1]]][dict1[arr[0]]] += int(arr[2])

ll = cnt

graph2=[[0 for _ in range(ll)] for _ in range (ll)]
while True:
    deq = deque()
    d=[-1 for _ in range(ll)]
    deq.append(dict1["A"])
    while deq:
        a=deq.popleft()
        for i in range(ll):
            if graph[a][i]-graph2[a][i]>0 and d[i]==-1:
                d[i]=a
                deq.append(i)
                if i==dict1["Z"]:
                    break
    if d[dict1["Z"]]==-1:
        break
    t=dict1["Z"]
    amount=1000000000
    while t!=dict1["A"]:
        amount=min(graph[d[t]][t]-graph2[d[t]][t],amount)
        t=d[t]
    t=dict1["Z"]
    while t!=dict1["A"]:
        graph2[d[t]][t]+=amount
        graph2[t][d[t]]-=amount
        t=d[t]
    ans+=amount

print(ans)