# 플레 5, 크루스칼, 플로이드 와샬, 40분
# 오랫만에 플레 문제를 풀었다. 구글링 없이 내 생각만으로 풀어서 좋았다.
# 문제가 플로이드 와샬로 정렬된 인접 행렬이 주어졌을 때, 인접 리스트 형태로
# 플로이드 와샬을 실행하기 전의 트리의 모양을 출력하는 것이었다.
# 어떻게 구할까 하다가, 최솟값부터 사이클이 만들어지지 않으면 인접 리스트에
# 넣으면 되겠구나 생각했고, 크루스칼의 유니온 파인드가 사이클을 확인하기에 조금만 수정해서 썼다.


def mst_kruskal(edges):
    global n

    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])

    def union(parent, rank, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    num_nodes = n
    parent = [i for i in range(num_nodes+1)]   # 부모를 저장하는데 초기에는 자기 자신이 부모다.
    result = []  # MST 에 포함된 간선들을 넣을 배열
    rank = [0]*(num_nodes+1)  # 트리의 높이
    close=[[] for _ in range(num_nodes+1)]

    while len(result) < num_nodes-1:
        w, u, v = edges.pop()
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            result.append([w, u, v])
            close[u].append(v)
            close[v].append(u)
            union(parent, rank, x, y)
    for i in range(1,n+1):
        close[i].sort()
        print(len(close[i]),*close[i])
    total_weight=0
    for w, u, v in result:
        total_weight += w
    return total_weight


n=int(input())
arr=[]
for i in range(1,n):
    tmp=[int(x) for x in input().split()]
    cnt = n
    while tmp:
        arr.append([tmp.pop(),i,cnt])
        cnt-=1
arr.sort(reverse=True)
mst_kruskal(arr)
