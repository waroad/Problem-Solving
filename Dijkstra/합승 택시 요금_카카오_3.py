# 카카오 기출, 다익스트라, 30분 좀 안되게 걸렸다.
# 문제를 보고 무엇으로 풀까하다가, 다익스트라 플로이드 와샬 둘 다 될 것 같았는데
# 그냥 다익스트라로 풀었다. 처음으로 제대로 된 다익스트라로 푼 것 같다.
# 기존까지는 그냥 제일 가중치 낮은 엣지 가져와가지고 그 엣지가 이미 갔던 노드가 아니면 사용하는 식으로 했는데,
# 이번에는 출발 노드를 정하고, 안간 노드 중에 거리가 가장 짧은 노드를 찾는 방식으로 했다.
# 시간복잡도는 뭐가 더 빠를지는 잘 모르겠다. 유의미한 차이가 있지는 않을 것 같다.

def solution(n, s, a, b, fares):
    arr=[[] for _ in range(n)]
    for fare in fares:
        arr[fare[0]-1].append([fare[1]-1,fare[2]])
        arr[fare[1]-1].append([fare[0]-1,fare[2]])

    def dijkstra(start):
        global base_distance
        visited={start:0}
        distance=[100000000]*n
        distance[start]=0
        cur=start
        while len(visited)<n:
            min_val=10000000000
            min_ind=-1
            for i in arr[cur]:
                if i[1]+distance[cur]<distance[i[0]]:
                    distance[i[0]]=i[1]+distance[cur]
            for ind,i in enumerate(distance):
                if ind not in visited and i<min_val:
                    min_val=i
                    min_ind=ind
            cur=min_ind
            visited[cur]=0
        if start==s-1:
            base_distance=distance[:]
        return distance[a-1]+distance[b-1]+base_distance[start]

    dijkstra(s - 1)
    ans=10000000
    for i in range(n):
        ans=min(ans,dijkstra(i))
    return ans
