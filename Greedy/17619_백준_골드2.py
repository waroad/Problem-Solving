# 그리디, union and find, 트리, 40분 정도
# 처음 문제를 딱 접했을 때는 어떻게 풀어야 되나 하고 고민을 하다가,
# 밑에 알고리즘에서 분리 집합이 있길래 그걸 검색해 봤더니 union and find 였다.
# 그걸 확정적으로 알고나니 아이디어가 바로 떠올랐고, 검색해보지 말걸 그랬다.
# 문제 자체는 그냥 kruskal 에 있는 union and find 함수를 그대로 가져와서
# 조금 응용해서 풀었다. 골드 2 치고는 신선했던 것 같다.
import sys
n,q=[int(x) for x in input().split()]
arr=[]
for i in range(n):
    tmp=[int(x) for x in sys.stdin.readline().split()]
    arr.append([tmp[0],tmp[1],i])
arr.sort()


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


parent = [i for i in range(n)]
result = []
rank = [0] * n
rank[0]=1
cur=arr[0][1]
cur_n=arr[0][2]
x=arr[0][2]
for i in range(1,n):
    if arr[i][0]<=cur:
        cur=max(cur,arr[i][1])
        union(parent, rank, x, arr[i][2])
    else:
        x=arr[i][2]
        cur=arr[i][1]
for j in range(q):
    tmp = [int(x) for x in sys.stdin.readline().split()]
    if find(parent, tmp[0]-1)== find(parent, tmp[1]-1):
        print(1)
    else:
        print(0)
