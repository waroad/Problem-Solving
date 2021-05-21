# 다익스트라 문제, 1시간 반 가량 걸렸다.
# 시작점에서 목적지까지의 최단거리가 특정 경로를 포함하는지를 묻는 문제이다.
# 제일 직관적인 방법은 시작점에서 특정 경로 좌표 중 하나까지의 거리 + 나머지 좌표에서 목적지까지의 값 +
# 특정 경로의 거리의 값이 시작점에서 목적지까지의 값과 같은지 비교하는 방법이겠지만, 너무 오래 걸릴 것 같아
# 다른 방법으로 짜보려다가 약 1시간동안 짜고 못풀었다. 결국 저 직관적인 방법으로 풀었다.
# 사실 아직도 왜 밑의 코드가 잘 안되는지 모르겠다. 힙에 넣을 때 하나의 변수를 추가해서 특정 경로를 지난 시점부터
# 그 이후에 최단거리가 정의되는 좌표들은 최단거리에 걸친다라고 풀려고 했는데 결국 안됐다.

import sys
from heapq import heappush, heappop

T=int(input())
for i in range(T):
    def comp(a, b):
        for j in range(0, len(arr[b])):
            if arr2[arr[b][j][0]]==1:
                continue
            if arr[b][j][1] + a < arr1[arr[b][j][0]]:
                arr1[arr[b][j][0]] = arr[b][j][1] + a
                heappush(heap, [arr[b][j][1] + a, arr[b][j][0]])


    N, E, D = [int(x) for x in input().split()]
    S, G, H= [int(x) for x in input().split()]
    arr = [[] for x in range(N)]
    arr1 = [2000000000] * N
    arr2 = [0] * N
    arr2[S - 1] = 1
    arr1[S - 1] = 0
    arr3 = [0] * N
    arrD=[]
    heap = []
    G-=1
    H-=1
    dist_G_H=0
    for i in range(0, E):
        tmp = [int(x) for x in sys.stdin.readline().split()]
        if (tmp[0]-1==G and tmp[1]-1==H) or (tmp[0]-1==H and tmp[1]-1==G):
            dist_G_H=tmp[2]
        arr[tmp[0] - 1].append([tmp[1] - 1, tmp[2]])
        arr[tmp[1] - 1].append([tmp[0] - 1, tmp[2]])

    for i in range(0, D):
        arrD.append(int(input()))
    comp(0, S - 1)
    arrD.sort()
    while heap:
        w, n = heappop(heap)
        comp(w, n)
    for i in range(len(arr1)):
        arr3[i]=arr1[i]
    for i in arrD:
        arr1 = [2000000000] * N
        arr2 = [0] * N
        arr2[i - 1] = 1
        arr1[i - 1] = 0
        comp(0, i-1)
        while heap:
            w, n = heappop(heap)
            comp(w, n)
        if min(arr3[G]+dist_G_H+arr1[H],arr3[H]+dist_G_H+arr1[G])==arr3[i-1]:
            print(i,end=' ')
    print("")
    
    
    
    
# 여기부터가 1시간동안 시도했지만 결국 틀린 방법이다.    
T=int(input())
for i in range(T):

    def comp(a, b, c):
        for j in range(0, len(arr[b])):
            if arr[b][j][1] + a <= arr1[arr[b][j][0]]:
                arr1[arr[b][j][0]] = arr[b][j][1] + a
                if (b == G and arr[b][j][0] == H) or (arr[b][j][0] == G and b == H):
                    heappush(heap, [arr[b][j][1] + a, arr[b][j][0], 1])
                else:
                    heappush(heap, [arr[b][j][1] + a, arr[b][j][0], c])


    N, E, D = [int(x) for x in input().split()]
    S, G, H= [int(x) for x in input().split()]
    arr = [[] for x in range(N)]
    arr1 = [2000000000] * N
    arr3 = [0] * N
    arr1[S - 1] = 0
    arrD=[]
    heap = []
    G-=1
    H-=1
    for i in range(0, E):
        tmp = [int(x) for x in sys.stdin.readline().split()]
        arr[tmp[0] - 1].append([tmp[1] - 1, tmp[2]])
        arr[tmp[1] - 1].append([tmp[0] - 1, tmp[2]])

    for i in range(0, D):
        arrD.append(int(input()))
    comp(0, S - 1, 0)
    arrD.sort()
    while heap:
        w, n, c = heappop(heap)
        comp(w, n, c)
        if c==1:
            arr3[n]=1
    for i in arrD:
        if arr3[i-1]==1:
            print(i,end=' ')
    print("")
