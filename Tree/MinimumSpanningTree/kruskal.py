# 나중에 쓰려고 기본형 하나 만들어 놨다.
# 구글꺼 가져와서 내가 읽기 쉽게 조금 수정한 것이다.
# 크루스칼은 sparse matrix 일 때 쓰면 좋다. 지금 이거는 2d 배열을 다시 edges 들로 쪼개서
# 배열안에 넣어주었는데, 입력 값이 애당초 edges 로 주어진다면 코드는 조금 더 짧아진다.

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

    while len(result) < num_nodes-1:
        w, u, v = edges.pop()
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            result.append([w, u, v])
            union(parent, rank, x, y)

    total_weight=0
    for w, u, v in result:
        total_weight += w
    return total_weight


arr_dis=[[0,4,5],
         [4,0,6],
         [5,6,0]]
ans = mst_kruskal(arr_dis)
print(ans)
