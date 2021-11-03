# 골드1, dp, tree, 1시간 정도
# 확실히 쌩 dp 가 아니라 tree 가 합쳐지니까
# 조금 더 어려운 것 같다. tree 의 특성을 곰곰히
# 생각해보면 풀 수 있는 문제이다. 이렇게 재귀함수로 문제를
# 푸는 것이 정말 오랫만인 것 같다.

import sys
sys.setrecursionlimit(10**6)
N=int(input())
arr_pop=[int(x) for x in input().split()]
arr_ans=[[-1,-1] for i in range(N)]
arr=[[] for _ in range(N)]
for i in range(N-1):
    tmp=[int(x) for x in sys.stdin.readline().split()]
    arr[tmp[0]-1].append(tmp[1]-1)
    arr[tmp[1]-1].append(tmp[0]-1)


def do(a,skip):
    if arr_ans[a][0]!=-1:
        return arr_ans[a]
    t1,t2=0,0
    for i in(arr[a]):
        if i!=skip:
            t1+=do(i,a)[1]
    for j in range(len(arr[a])):
        t2_t=0
        for ind,k in enumerate(arr[a]):
            if k==skip:
                continue
            if ind==j:
                t2_t+=do(k,a)[0]
            else:
                t2_t+=max(do(k,a))
        t2=max(t2_t,t2)
    arr_ans[a]=[t1+arr_pop[a],t2]
    return arr_ans[a]


print(max(do(0,-1)))
