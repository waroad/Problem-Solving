# 골드 3, 배낭 문제, 1시간 반.
# 이거 말고 좀 이상하게 원래 풀었는데, 실행 시간이 너무 오래 걸려서 인터넷으로 찾아보니
# 역시나 더 효율적인 방법이 있었다.
# 그래서 그 방법으로 다시 풀었다.
N,M=[int(x) for x in input().split()]
value=[int(x) for x in input().split()]
cost=[int(x) for x in input().split()]
dp=[[0 for k in range(0,sum(cost)+1)] for x in range(0,N+1)]
for i in range(0,N):
    for j in range(0, cost[i]+1):
        dp[i+1][j]=dp[i][j]
    for j in range(0,sum(cost)-cost[i]+1):
        dp[i+1][j+cost[i]]=max(dp[i][j+cost[i]],dp[i][j]+value[i])
for i in range(0,sum(cost)+1):
    if dp[N][i]>=M:
        print(i)
        break
