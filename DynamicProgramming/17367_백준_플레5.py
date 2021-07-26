# 플레5, 다이나믹 프로그래밍 및 확률, 3시간
# 느긋느긋하게 풀긴 했어도 3시간 걸렸다. 
# 이 문제는 UCPC 문제로, 처음부터 풀 수 있을꺼라 기대하기 보다는,
# 구글링도 좀 하면서 가이드를 얻어가면서 풀어봐야지 하는 느낌으로 시도했다.
# 기댓값, 확률 문제를 정말 오랫만에 접해서 감을 못잡았는데 (처음일수도) 그냥 모든 경우의 수를 구해서
# 나눠주는 식으로 푼다는 것을 알았다. 구글링 해보니 다 dp로 dp[n][6][6][6]의 배열로 풀었는데,
# dp[n][6][6]으로 풀 수 있을 것 같아서 그렇게 풀었다가, 결국 실패했다. 일단 질문글을 올리긴 했는데
# 그래서 결국은 나도 구글에 나온 방식대로 이해하면서 배운다는 느낌으로 풀었다.
N=int(input())
dp2 =[[[[0.0]*6 for _ in range(6)] for _ in range(6)] for _ in range(N)]
ans=0


def prize(i,j,k):
    if i == j == k:
        return 10000 + (k + 1) * 1000
    elif i == j:
        return 1000 + (j + 1) * 100
    elif i == k:
        return 1000 + (k + 1) * 100
    elif j == k:
        return 1000 + (k + 1) * 100
    else:
        return (max([i, j, k]) + 1) * 100


for n in range(N-2):
    for i in range(6):
        for j in range(6):
            for k in range(6):
                if n == 0:
                    dp2[n][i][j][k] = prize(i, j, k)
                else:
                    tmp= sum(dp2[n - 1][j][k]) / 6
                    if dp2[n - 1][i][j][k]>tmp:
                        dp2[n][i][j][k] = dp2[n - 1][i][j][k]
                    else:
                        dp2[n][i][j][k] = tmp


for i in range(6):
    for j in range(6):
        ans += sum(dp2[N-3][i][j])
print(ans/216)
