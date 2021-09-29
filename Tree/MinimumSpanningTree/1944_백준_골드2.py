# 골드2, MST, 프림, 1시간 20분
# 난이도는 적당하다. 이거 하느라 오랫만에 MST를 했는데,
# 일단 프림은 구글에서 긁어왔다. 내일은 프림과 크루스칼 기본형 문제를 풀어서 올려야겠다.



from collections import deque

n, m = [int(x) for x in input().split()]
arr = [[x for x in input()] for _ in range(n)]
arr_dis = [[1000000000 for _ in range(m + 1)] for _ in range(m + 1)]
cnt = 2
nodes = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'S' or arr[i][j] == 'K':
            arr[i][j] = str(cnt)
            cnt += 1
            nodes.append([i, j])

std_arr = [arr[x][:] for x in range(n)]


def find(x, y):
    global cnt
    queue = deque()
    queue.append([x, y, 1])
    arr[x][y]='1'
    while queue:
        x, y, m = queue.popleft()
        if x > 1 and arr[x - 1][y] != '1':
            if arr[x - 1][y] == '0':
                queue.append([x - 1, y, m + 1])
            else:
                arr_dis[cnt][int(arr[x - 1][y]) - 2] = m
                arr_dis[int(arr[x - 1][y]) - 2][cnt] = m
            arr[x - 1][y]='1'
        if x < n - 2 and arr[x + 1][y] != '1':
            if arr[x + 1][y] == '0':
                queue.append([x + 1, y, m + 1])
            else:
                arr_dis[cnt][int(arr[x + 1][y]) - 2] = m
                arr_dis[int(arr[x + 1][y]) - 2][cnt] = m
            arr[x + 1][y]='1'
        if y > 1 and arr[x][y - 1] != '1':
            if arr[x][y - 1] == '0':
                queue.append([x, y - 1, m + 1])
            else:
                arr_dis[cnt][int(arr[x][y - 1]) - 2] = m
                arr_dis[int(arr[x][y - 1]) - 2][cnt] = m
            arr[x][y-1]='1'
        if y < n - 2 and arr[x][y + 1] != '1':
            if arr[x][y + 1] == '0':
                queue.append([x, y + 1, m + 1])
            else:
                arr_dis[cnt][int(arr[x][y + 1]) - 2] = m
                arr_dis[int(arr[x][y + 1]) - 2][cnt] = m
            arr[x][y+1]='1'


cnt = 0
for node in nodes:
    find(node[0], node[1])
    cnt += 1
    arr = [std_arr[x][:] for x in range(n)]

# for i in range(n):
#     print(arr[i])
# print("")
# for i in range(n):
#     print(std_arr[i])
# for i in range(m + 1):
#     print(arr_dis[i])
# 프림 알고리즘

INF = float('inf')

# 각 정점 사이의 가중치가 주어진다.

# 집합 S: 최종적으로 만들어질 트리. 처음에는 아무것도 포함되지 않았다고 가정한다.
# 프림 알고리즘에서는 모든 정점에 대해 S와의 거리를 저장한 dist라는 배열을 두고, 이 중 가장 가까운 정점을 S에 하나씩 포함시킨다.
# 새로 포함된 정점 때문에 그 정점에 인접한 점들은 S에 포함될 수 있는 최단거리가 갱신될 수 있으므로 확인 후 갱신한다.

V_NUM = len(arr_dis[0])
dist = [INF for _ in range(V_NUM)]  # 모든 정점에 대해서 집합 S와의 최단거리. 처음에는 모두 무한대라고 가정한다.
selected = [False for _ in range(V_NUM)]
dist[0] = 0  # 시작 정점을 선택하고 S에 포함하고, 거리가 0이라고 가정한다. (프림 알고리즘의 시작)

for _ in range(V_NUM):  # 정점의 갯수만큼 반복

    unselected = [idx for idx, val in enumerate(selected) if not val]
    u = min(unselected, key=lambda x: dist[x])
    # u=아직 집합 S에 포함되지 않은 정점 중에서 집합에 연결되기 위해 최소 비용이 드는 점을 구한다.

    selected[u] = True

    for v in range(V_NUM):
        if arr_dis[u][v] != INF:  # u와 연결된 정점 중에서
            if not selected[v] and arr_dis[u][v] < dist[v]:
                # S에 포함되지 않은 정점 중에서,
                # 이미 알려진 길(dist[v])보다 더 가까운 길로 갈 수 있으면(arr_dis[u][v]) 갱신한다. 다음에 방문하기 위해서..
                dist[v] = arr_dis[u][v]
if sum(dist)>=1000000000:
    print(-1)
else:
    print(sum(dist))
