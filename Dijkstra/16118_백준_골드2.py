# 다익스트라, 실제로 코딩한 시간은 약 1시간, 이걸로 쓴 시간은 약 5시간
# 이 문제는 파이썬에 추가 시간이 안 붙어있는, 옛날 문제였다.
# 그래서 질문 칸에도 파이썬 시간초과에 관한 글이 많았고, 실제로 파이썬으로 맞힌 사람이 4명밖에 안됐었다.
# 그 중 하나가 구글에 올라와 있길래 비교해봤더니 역시나 나랑 코드가 별 차이가 없었다.
# 이래저래 조금씩 수정하면서 수십번 올리다가 결정적으로 24번 줄과 37번 줄에 있는 cnt를 넣으면서 풀 수 있었다.
# cnt로 모든 노드가 최단거리로 완성되면, 힙에 남아 있어도 루프를 탈출하게 해주는 구문이다. 그래도 풀어서 다행이다.

import sys
from heapq import heappush, heappop

N, E = [int(x) for x in sys.stdin.readline().split()]
arr = [[] for _ in range(N)]
arr1 = [1000000001 for _ in range(N)]
arr3 = [[1000000001 for _ in range(N)] for _ in range(2)]
arr1[0] = 0
arr3[1][0]=0
heap = []
for i in range(0, E):
    a,b,c = [int(x) for x in sys.stdin.readline().split()]
    arr[a - 1].append([b - 1, c*2])
    arr[b - 1].append([a - 1, c*2])
heappush(heap,[0,0])
cnt=N-1
while heap and cnt:
    a, b = heappop(heap)
    if a>arr1[b]:
        continue
    for j in (arr[b]):
        if j[1] + a < arr1[j[0]]:
            arr1[j[0]] = j[1] + a
            heappush(heap, [j[1] + a, j[0]])
    cnt-=1
heap=[]
heappush(heap,[0,0,0])

cnt=2*N-1
while heap and cnt:
    a, b, c = heappop(heap)
    if a>arr3[(c+1)%2][b]:
        continue
    for j in (arr[b]):
        tmp = int((c * 1.5 + 0.5) * j[1]) + a
        if tmp < arr3[c][j[0]]:
            arr3[c][j[0]] = tmp
            heappush(heap, [tmp, j[0], (c + 1) % 2])
    cnt-=1
cnt=0
for i in range(N):
    if arr1[i]<arr3[0][i] and arr1[i]<arr3[1][i]:
        cnt+=1
sys.stdout.write(str(cnt))
