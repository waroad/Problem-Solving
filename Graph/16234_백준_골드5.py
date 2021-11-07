# 골드 5, 그래프, BFS, 20분 정도
# 그냥 BFS 문제이다. 
# 더 이상 할 말이 없다.
import sys
n,l,r=[int(x) for x in input().split()]
arr=[[int(x) for x in input().split()] for _ in range(n)]
sys.setrecursionlimit(10**6)


def go(a,b,c):
    if a>0 and arr_group[a-1][b]==0 and  l<=abs(arr[a][b]-arr[a-1][b])<=r:
        arr_sum[c][0]+=arr[a-1][b]
        arr_sum[c][1]+=1
        arr_group[a - 1][b] =c
        go(a-1,b,c)
    if b > 0 and arr_group[a][b-1] == 0 and l <= abs(arr[a][b] - arr[a][b-1]) <= r:
        arr_sum[c][0] += arr[a][b-1]
        arr_sum[c][1]+=1
        arr_group[a][b - 1]=c
        go(a, b-1, c)
    if a<n-1 and arr_group[a+1][b]==0 and  l<=abs(arr[a][b]-arr[a+1][b])<=r:
        arr_sum[c][0]+=arr[a+1][b]
        arr_sum[c][1]+=1
        arr_group[a + 1][b]=c
        go(a+1,b,c)
    if b <n-1 and arr_group[a][b+1] == 0 and l <= abs(arr[a][b] - arr[a][b+1]) <= r:
        arr_sum[c][0] += arr[a][b+1]
        arr_sum[c][1]+=1
        arr_group[a][b + 1]=c
        go(a, b+1, c)


ans=0
while True:
    cnt=1
    arr_group=[[0 for _ in range(n)] for _ in range(n)]
    arr_sum=[[0, 0] for _ in range(n*n+1)]
    for i in range(n):
        for j in range(n):
            if arr_group[i][j]==0:
                arr_sum[cnt][0]+=arr[i][j]
                arr_sum[cnt][1]+=1
                arr_group[i][j]=cnt
                go(i,j,cnt)
                cnt+=1

    # for i in range(n):
    #     print(arr_group[i])
    # print(arr_sum)
    if cnt==n*n+1:
        break
    ans+=1
    for i in range(n):
        for j in range(n):
            arr[i][j]=arr_sum[arr_group[i][j]][0]//arr_sum[arr_group[i][j]][1]

print(ans)
