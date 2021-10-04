# 골드 2, 크루스칼, 30분
# 크루스칼은 가지고 있는 것을 그대로 썼다.
# 시간이 좀 오래 걸린 이유는 문제에서 소문자가 대문자 보다 값이 작은데,
# ord 로 하니까 소문자가 오히려 더 나중에 와서 값이 더 크게 설정해서 그거 모르느라 좀 걸렸다.
# 그리고 이전까지는 lambda 를 쓴 적이 없는데, 이번에 처음 써봤다.
# 단순히 list comprehension 으로는 if 를 쓸 수가 없어서 썼다.
# 그리고 양방향 그래프에서 x->y , y->x 의 값이 다를 경우는 프림 말고 크루스칼을 써야 한다는 것을
# 알았다. 문제 자체는 쉽다.

def mst_kruskal(graph):
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

    num_nodes = len(graph)
    parent = [i for i in range(num_nodes)]   # 부모를 저장하는데 초기에는 자기 자신이 부모다.
    result = []  # MST 에 포함된 간선들을 넣을 배열
    rank = [0]*num_nodes  # 트리의 높이
    edges = []
    for i in range(num_nodes):
        for j in range(num_nodes):
            if graph[i][j] > 0:
                edges.append([graph[i][j], i, j])

    edges.sort(reverse=True)  # 리버스로 정렬해서, 뒤에서부터 pop 해서 최소 무게의 edge 부터 가져온다.
    while len(result) < num_nodes-1 and edges:
        w, u, v = edges.pop()
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            result.append([w, u, v])
            union(parent, rank, x, y)
    if len(result) < num_nodes-1:
        return -1
    total_weight=0
    for w, u, v in result:
        total_weight += w
    return total_weight


n=int(input())
arr=[[(lambda t: 0 if ord(t)==48 else (ord(t)-38)%58)(t) for t in list(input())] for _ in range(n)]
sum1=sum([sum(i) for i in arr])
ans = mst_kruskal(arr)
if ans==-1:
    print(-1)
else:
    print(sum1-ans)
