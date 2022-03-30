# dp 로 길 찾는 매우 기본적인 문제.
# 딱히 더 할 말도 없다.
from collections import deque


def solution(m,n,puddles):
    dp=[[0 for _ in range(m)] for _ in range(n)]
    obstacleGrid=[[0 for _ in range(m)] for _ in range(n)]
    for i in puddles:
        obstacleGrid[i[1]-1][i[0]-1]=1
    dp[0][0]=1
    deq = deque()
    deq.appendleft([0,0])
    while deq:
        a,b=deq.pop()
        if a+1<n and obstacleGrid[a+1][b]!=1:
            dp[a+1][b]+=dp[a][b]
        if b+1<m and obstacleGrid[a][b+1]!=1:
            dp[a][b+1]+=dp[a][b]
        if a+1<n:
            deq.appendleft([a+1,b])
        if a==0 and b+1<m:
            deq.appendleft([a,b+1])
    return dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1]%1000000007


print(solution( 4,3, [[2, 2]]))