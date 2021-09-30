# 골드 2, mst, 15분
# 이 문제는 프림으로 풀어도, 크루스칼로 풀어도 상관없다. 프림으로 처음에 15분 만에 풀고
# 크루스칼로 다시 풀어봤다. 크루스칼도 구글에서 가져와서 내가 편한대로 조금 수정했다.
# 이 문제도 거의 기본문제이다. 
n=int(input())
arr=[int(input()) for _ in range(n)]
arr2=[[int(x) for x in input().split()] for _ in range(n)]

arr2.append(arr)
for i in range(n):
    arr2[i].append(arr[i])
arr2[n].append(0)


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


ans = mst_kruskal(arr2)
print(ans)

