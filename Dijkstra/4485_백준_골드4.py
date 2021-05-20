# 다익스트라 문제, 골드 4
# n*n 크기의 2차원 배열에 각기 다른 값이 저장되어 있고, 0,0부터 n-1,n-1까지 가는데 어떻게 가야
# 최소한의 값만 가져가는지 묻는 다익스트라, 그래프 문제이다.
# 이런 류의 문제가 나오면 지금까지는 해당 좌표의 누적 값보다 현재 누적 값 + 해당 좌표의 값이 더 작을 경우
# 값을 업데이트 하고 큐에 넣어서 다시 해주는 방식을 사용했는데, 시간초과가 났다.
# 이것도 heapq 에 넣으니 바로 풀렸다. 두 개가 시간복잡도의 차이가 크다는 것을 너무 늦게 안 것 같다.

import sys,heapq

cnt=1
while True:
    n=int(input())
    if n==0:break
    arr=[[int(x) for x in sys.stdin.readline().split()] for y in range(n)]
    arr1=[[10000000 for x in range(n)] for y in range(n)]
    arr1[0][0]=arr[0][0]
    que=[]
    heapq.heappush(que,[arr[0][0],0,0])
    while len(que):
        tmp=heapq.heappop(que)
        if tmp[1]<n-1:
            if arr[tmp[1]+1][tmp[2]]+arr1[tmp[1]][tmp[2]]<arr1[tmp[1]+1][tmp[2]]:
                arr1[tmp[1]+1][tmp[2]]= arr[tmp[1]+1][tmp[2]]+arr1[tmp[1]][tmp[2]]
                heapq.heappush(que, [arr1[tmp[1]+1][tmp[2]],tmp[1]+1,tmp[2]])
        if tmp[1]>0:
            if arr[tmp[1]-1][tmp[2]]+arr1[tmp[1]][tmp[2]]<arr1[tmp[1]-1][tmp[2]]:
                arr1[tmp[1]-1][tmp[2]]= arr[tmp[1]-1][tmp[2]]+arr1[tmp[1]][tmp[2]]
                heapq.heappush(que, [arr1[tmp[1]-1][tmp[2]],tmp[1]-1,tmp[2]])
        if tmp[2] < n - 1:
            if arr[tmp[1]][tmp[2]+1] + arr1[tmp[1]][tmp[2]] < arr1[tmp[1]][tmp[2]+1]:
                arr1[tmp[1]][tmp[2]+1] = arr[tmp[1]][tmp[2]+1] + arr1[tmp[1]][tmp[2]]
                heapq.heappush(que, [arr1[tmp[1]][tmp[2]+1], tmp[1], tmp[2]+1])
        if tmp[2] > 0:
            if arr[tmp[1]][tmp[2]-1] + arr1[tmp[1]][tmp[2]] < arr1[tmp[1]][tmp[2]-1]:
                arr1[tmp[1]][tmp[2]-1] = arr[tmp[1]][tmp[2]-1] + arr1[tmp[1]][tmp[2]]
                heapq.heappush(que, [arr1[tmp[1]][tmp[2]-1], tmp[1], tmp[2]-1])

    print("Problem",cnt,end='')
    print(":",arr1[n-1][n-1])
    cnt+=1
