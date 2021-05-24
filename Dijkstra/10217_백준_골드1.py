# 골드 1, 다익스트라지만 다익스트라가 아닌 문제.
# 이 문제에 3시간 넘게 쏟았다. 이렇게 안풀리기도 오랫만인 것 같다.
# 다익스트라 문제 답게 처음에 heapq 을 써서 풀었는데 계속 시간초과가 나고 진전이 없어서 고민하다가
# 게시판을 조금 뒤져보니 이걸 queue 말고 그냥 for 구문으로 풀었다는 말이 있어서
# 결국 그 방법 따라서 for 구문으로 풀었다. 저걸 heapq 로 바꿔서, cost 우선선위로 풀어도
# 이번엔 메모리 초과가 나서 모르겠다.

import sys
from queue import Queue
TT=int(input())
for l in range(TT):

    N,M, E = [int(x) for x in sys.stdin.readline().split()]
    arr = [[] for _ in range(N)]
    arr2= [[0 for _ in range(M+1)] for _ in range(N)]
    arr3=[[200000000 for _ in range(M+1)] for _ in range(N)]
    for i in range(0, E):
        a,b,c,T = [int(x) for x in sys.stdin.readline().split()]
        arr[a - 1].append([b - 1, T,c])
    for j in (arr[0]):
        if j[2] > M: continue
        if j[1] + 0 < arr3[j[0]][j[2]]:
            arr3[j[0]][j[2]] = j[1]
    for c in range(M + 1):
        for b in range(N):
            if arr3[b][c]==200000000: continue
            for j in (arr[b]):
                if c + j[2] > M: continue
                if j[1]+arr3[b][c]<arr3[j[0]][c+j[2]]:
                    arr3[j[0]][c+j[2]]=j[1]+arr3[b][c]

    tmp= min(arr3[N-1])
    if tmp!=200000000: print(tmp)
    else: print("Poor KCM")
