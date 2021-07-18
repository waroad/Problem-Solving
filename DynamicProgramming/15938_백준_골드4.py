# 골드 4, 다이나믹 프로그래밍, 1시간 좀 넘게 걸렸다.
# 이것도 UCPC라 그런지는 모르겠지만 골드 4 치고는 어려웠던 것 같ㄷ가.
# 단순한 dp 문제이긴 한데, 내가 좀 헛짓거리를 한 것도 있긴하다.
# 이 문제는 deepcopy로 풀었는데 시간초과가 떠서, 그걸 그냥 메모리를 더 잡아먹더라도
# 3차원 배열에 다 따로따로 저장했는데 그랬더니 맞았다.

import sys
x,y = [int(z) for z in input().split()]
T=int(input())
x_des,y_des=[int(z) for z in input().split()]
num_of_obs=int(input())
arr=[[[0 for z in range(401)] for x in range(401)] for y in range(T+1)]
for i in range (num_of_obs):
    t1,t2=[int(x) for x in sys.stdin.readline().split()]
    if 0<=t1-x+200<401 and 0<=t2-y+200<401:
        for j in range(T+1):
            arr[j][t1-x+200][t2-y+200]=-1
arr[0][200][200]=1
Time=0
ans=0

if 0<=x_des-x+200<401 and 0<=y_des-y+200<401:
    while Time<T:
        for i in range(401):
            for j in range(abs(200-i),401-abs(200-i)):
                if arr[Time][i][j]>0:
                    if i>0 and arr[Time][i-1][j]!=-1:
                        arr[Time+1][i-1][j]+=arr[Time][i][j]
                        arr[Time+1][i-1][j]%=1000000007
                    if i<400 and arr[Time][i+1][j]!=-1:
                        arr[Time+1][i+1][j]+=arr[Time][i][j]
                        arr[Time+1][i+1][j]%=1000000007
                    if j>0 and arr[Time][i][j-1]!=-1:
                        arr[Time+1][i][j-1]+=arr[Time][i][j]
                        arr[Time+1][i][j-1]%=1000000007
                    if j<400 and arr[Time][i][j+1]!=-1:
                        arr[Time+1][i][j+1]+=arr[Time][i][j]
                        arr[Time+1][i][j+1]%=1000000007
        ans+=arr[Time+1][x_des - x+200][y_des - y+200]
        ans%=1000000007
        arr[Time+1][x_des - x+200][y_des - y+200]=0
        Time+=1
print(ans)


