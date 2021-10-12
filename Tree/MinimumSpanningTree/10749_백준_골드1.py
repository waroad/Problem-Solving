# 골드 1, mst, 20분
# 이번 문제는 maximum spanning tree 를 찾기만 하면 되는 다소 간단한 문제였다.
# 단 2000개의 노드가 모두 서로를 향한 edge 가 있기에, kruskal 로는 시간초과가 나고
# prim 으로 통과가 가능하다.
# 처음으로 영어로만 된 문제를 풀어봤다.
from operator import xor
n=int(input())
arr=[int(input()) for _ in range(n)]
arr2=[[0 for _ in range(n)] for _ in range(n)]


def mst_prim(G, s):
    N = len(G)
    key = [0] * N  # 가중치를 무한대로 초기화
    visited = [0] * N  # 방문 여부 초기화
    key[s] = 0  # 시작 정점의 가중치를 0으로 설정
    for _ in range(N):  # 정점의 개수만큼 반복
        minIndex = -1
        min = -1
        for i in range(N):  # 방문 안한 정점 중 최소 가중치 정점 찾기
            if not visited[i] and key[i] > min:
                min = key[i]
                minIndex = i
        visited[minIndex] = True  # 최소 가중치 정점 방문처리
        for v in range(N):  # 선택 정점의 인접한 정점에 대해서
            if not visited[v] and G[minIndex][v] > key[v]:
                key[v] = G[minIndex][v]  # 가중치 갱신
    return sum(key)


for i in range(n):
    for j in range(n):
        arr2[i][j]=xor((arr[i]),(arr[j]))

print(mst_prim(arr2,0))
