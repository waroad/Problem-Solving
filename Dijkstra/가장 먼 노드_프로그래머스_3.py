# 다익스트라 문제, 15분 남짓.
# 오랫만에 다익스트라나 한번 풀어봤다.
# 2차원 sparse matrix 형태가 아니라 그냥 배열로 왔고, 모든 노드의 값이
# 1이라는 것이 약간 다르다. 그래서 오히려 더 쉬웠던 것도 같다.
# 다익스트라는 한 노드에서 모든 노드까지의 최단 거리, 플로이드 와샬은 모든 노드에서 모든 노드까지의 최단거리,
# mst 는 그래프에서 모든 정점을 포함하는 최소 그래프이다!

from collections import deque


def solution(n, edge):
    dijk=[[] for _ in range(n)]
    dijk_len=[100000000]*n
    dijk_len[0]=0
    for i in edge:
        dijk[i[0]-1].append(i[1]-1)
        dijk[i[1]-1].append(i[0]-1)

    deq = deque()
    deq.append(0)
    while len(deq):
        tmp=deq.popleft()
        for i in dijk[tmp]:
            if dijk_len[i]>dijk_len[tmp]+1:
                dijk_len[i]=dijk_len[tmp]+1
                deq.append(i)
    answer = 0
    for i in range(n):
        if dijk_len[i]==max(dijk_len):
            answer+=1
    return answer


solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])