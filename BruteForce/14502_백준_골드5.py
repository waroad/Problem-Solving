# 골드 5, 브루트 포스랑 BFS, 25분
# 골드 5인데도 생각보단 오래 걸렸다. 그냥 한번 풀어봤다.
# 넘피가 요즘 코딩테스트 환경에서 지원되지 않는 것이 아쉽다.
# 2차원 배열 전체 복사를 할 때 앞으로도 구글링을 먼저 해봐야겠다.
n,m=[int(x) for x in input().split()]
arr=[[int(x) for x in input().split()] for _ in range(n)]
virus_cor=[]

ans=0
for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            virus_cor.append([i,j])


def spread(a,b):
    if a+1<n and arr[a+1][b]==0:
        arr[a+1][b]=2
        spread(a+1,b)
    if a-1>=0 and arr[a-1][b]==0:
        arr[a-1][b]=2
        spread(a-1,b)
    if b+1<m and arr[a][b+1]==0:
        arr[a][b+1]=2
        spread(a,b+1)
    if b - 1 >= 0 and arr[a][b - 1] == 0:
        arr[a][b - 1] = 2
        spread(a, b - 1)


def virus():
    global ans,arr
    arr1 = [row[:] for row in arr]  # 배열 전체 복사
    for vi in virus_cor:
        spread(vi[0],vi[1])
    cnt=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                cnt+=1
    if cnt>ans:
        ans=cnt
    arr = [row[:] for row in arr1]  # 다시 확산 전 배열로 변경


def case(a,b,cnt1):
    if cnt1==0:
        virus()
        return
    for i in range(a,n):
        for j in range(m):
            if i==a and j<b:
                continue
            if arr[i][j]==0:
                arr[i][j]=1
                case(i,j+1,cnt1-1)
                arr[i][j]=0


case(0,0,3)
print(ans)
