# 골드 3, 플로이드 와샬, 30분(개념 읽는거 포함)
# 어제 풀었던 문제를 플로이드 와샬로 다시 풀었다.
# 확실히 이게 조금 더 수행시간도 빠르고 코드가 간결하다.
# 앞의 일어난 사건과 상관관계를 아는 것은 위상정렬 밖에 없는 줄 알았는데
# 플로이드 와샬도 응용하니 이런식으로 가능하다는 것을 알았다.
# 상관관계를 플로이드 와샬로 어떻게 풀었냐면, 앞에서 뒤로 가는 관계를
# 엣지로 하는 한방향 그래프를 만들어서 최단거리를 구하여서, 최단거리가
# 무한이 아니면 상관관계인 것이다.
import sys

n, k = [int(x) for x in input().split()]
arr = [[1000000000 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(k):
    tmp = [int(x) for x in sys.stdin.readline().split()]
    arr[tmp[0]][tmp[1]] = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            arr[j][k]=min(arr[j][k],arr[j][i]+arr[i][k])
k = int(input())
for i in range(k):
    tmp = [int(x) for x in sys.stdin.readline().split()]
    if arr[tmp[0]][tmp[1]]<1000000000:
        print(-1)
    elif arr[tmp[1]][tmp[0]] < 1000000000:
        print(1)
    else:
        print(0)
