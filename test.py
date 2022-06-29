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



print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))