# 골드 1, dp, 비트마스킹, 1시간 정도
# 드디어 숙원의 외판원 순회를 풀었다. 풀이는 이미 대충
# 알고 있었어서, 블로그의 해석을 참고해 그냥 정석대로 풀었다. 
# vis 에 [현재 위치][방문한 노드들]을 넣어서 dp로 풀었다.
# 코드는 다 직접 짜기는 했다. 이제 비트마스킹을 쭉쭉 풀어봐야겠다.
import itertools

N = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]
vis = [[100000000 for _ in range(2 ** N)] for _ in range(N)]
comb = [i for i in range(1, N)]
for i in range(N):
    if arr[0][i] != 0:
        vis[i][2 ** i + 1] = arr[0][i]
for i in range(2, N):
    tmp = list(itertools.combinations(comb, i))
    for k in tmp:
        tt = sum(2 ** p for p in k) + 1
        for j in k:
            min_t = 100000000
            for l in k:
                if l != j and arr[l][j]:
                    min_t = min(min_t, vis[l][tt - 2 ** j] + arr[l][j])
            vis[j][tt] = min_t

ans = 100000000
for i in range(N):
    if arr[i][0]:
        ans = min(ans, vis[i][2 ** N - 1] + arr[i][0])
print(ans)
