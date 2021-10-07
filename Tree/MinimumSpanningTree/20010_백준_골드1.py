# 골드 1, 크루스칼, 트리, 20분 정도.
# 사실 이 문제는 골드 1이긴 하지만, 그냥 골드 2 + 골드 3 문제이다.
# 문제에서 처음에 mst 를 물어보는데 그냥 크루스칼로 짜면 되고,
# 그 다음 mst 에서 최장 거리 즉 트리의 지름을 물어보는데
# 이거는 전에 풀었던 적이 있어서 코드를 그대로 가져와서 넣었다.
# 전에 짰던 코드가 한번 활용됐다는 것이 좋았다.
# https://www.acmicpc.net/problem/1167 문제가 트리 지름 문제이다.

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
    parent = [i for i in range(num_nodes)]   # 부모를 저장하는데 초기에는 자기 자신이 부모다.
    result = []  # MST 에 포함된 간선들을 넣을 배열
    rank = [0]*(num_nodes)  # 트리의 높이
    close=[[] for _ in range(num_nodes)]

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
    return total_weight,result


def dfs(a):
    global ans,maxL,maxI
    arr1[a]=1
    if ans>maxL:
        maxL=ans
        maxI=a
    for i in range(len(arr2[a])):
        if arr1[arr2[a][i][0]]==1:
            continue
        ans+=arr2[a][i][1]
        dfs(arr2[a][i][0])
        ans-=arr2[a][i][1]


n,m=[int(x) for x in input().split()]
arr=[]
for i in range(m):
    tmp=[int(x) for x in input().split()]
    arr.append([tmp[2],tmp[0],tmp[1]])
arr.sort(reverse=True)
mst,arr_t=mst_kruskal(arr)
arr2=[[] for _ in range(n)]
for i in arr_t:
    arr2[i[1]].append([i[2],i[0]])
    arr2[i[2]].append([i[1],i[0]])
ans=0
maxL=0
maxI=-1
arr1=[0]*(n+1)
dfs(0)
ans=0
maxL=0
arr1=[0]*(n+1)
dfs(maxI)
print(mst)
print(maxL)
