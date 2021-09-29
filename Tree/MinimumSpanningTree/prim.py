# 나중에 쓰려고 기본형 하나 만들어 놨다.
# 구글꺼 가져와서 내가 읽기 쉽게 조금 수정한 것이다.


def mst_prim(G, s):
    N = len(G)
    key = [1000000000] * N  # 가중치를 무한대로 초기화
    visited = [0] * N  # 방문 여부 초기화
    key[s] = 0  # 시작 정점의 가중치를 0으로 설정
    for _ in range(N):  # 정점의 개수만큼 반복
        minIndex = -1
        min = 1000000000
        for i in range(N):  # 방문 안한 정점 중 최소 가중치 정점 찾기
            if not visited[i] and key[i] < min:
                min = key[i]
                minIndex = i
        visited[minIndex] = True  # 최소 가중치 정점 방문처리
        for v in range(N):  # 선택 정점의 인접한 정점에 대해서
            if not visited[v] and G[minIndex][v] < key[v]:
                key[v] = G[minIndex][v]  # 가중치 갱신
    return sum(key)


arr_dis=[[0,4,5],
         [4,0,6],
         [5,6,0]]
ans = mst_prim(arr_dis, 0)
