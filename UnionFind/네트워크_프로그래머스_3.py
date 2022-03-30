# 문제 분류가 dfs/bfs 로 되어있고, 나도 다 풀고 나니 dfs/bfs 로 좀 더 간단하게 가능하겠구나
# 깨달았다. 그래도 뭐 일단 union-find 로 풀었으니 됐다.

def solution(n, computers):
    par=[i for i in range(n)]
    level = [0 for _ in range(n)]

    def find_root(a1):
        while par[a1] != a1:
            a1 = par[a1]
        return a1

    def con(a, b):
        a1 = find_root(a)
        b1= find_root(b)
        if par[a1]==par[b1]:
            return
        else:
            if level[a1]>level[b1]:
                par[b1]=a1
                par[b]=a1
            else:
                par[a1]=b1
                par[a]=b1
                if level[a1]==level[b1]:
                    level[b1]+=1

    for i in range(n):
        for j in range(i):
            if computers[i][j]==1:
                con(i,j)
    ans_list=[]
    for i in range(n):
        tmp=find_root(i)
        if tmp not in ans_list:
            ans_list.append(tmp)
    return len(ans_list)


solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	)