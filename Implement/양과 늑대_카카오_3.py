# 30분, dfs 구현 문제이다.
# 모든 경우의 수를 탐색하면 되는데, BFS로의 메리트가 없어 보여서 DFS로 구현했다.
# 노드 수가 17개라서, 시간복잡도를 사실 더 줄이려면 줄일 수있는데 안줄이고 그냥 해봤는데 통과해서
# 저대로 냅뒀다. 아이디어만 잡으면 구현하기 쉬운 문제였다.
# 어제 skt 인턴 최종 면접에서 또 떨어졌다. 면접을 따로 준비를 더 해야할 것 같다.
# 아쉬웠다.
ans=0


def solution(info, edges):
    global ans
    arr=[[] for _ in range(len(info))]
    for i in edges:
        arr[i[0]].append(i[1])
        arr[i[1]].append(i[0])
    visited={0:0}

    def dfs(edges1,wolf_cnt,sheep_cnt):
        global ans
        edges2=edges1[:]
        if wolf_cnt>=sheep_cnt:
            return
        for edge in edges1:
            for i in arr[edge]:
                if i not in visited:
                    visited[i]=0
                    edges2.append(i)
                    if info[i]==0:
                        ans=max(ans,sheep_cnt+1)
                        dfs(edges2,wolf_cnt,sheep_cnt+1)
                    else:
                        if wolf_cnt < sheep_cnt:
                            dfs(edges2, wolf_cnt+1, sheep_cnt)
                    visited.pop(i)
                    edges2.pop()

    dfs([0],0,1)

    return ans

