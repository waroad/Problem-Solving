# 그리디, 골드 2 문제, 30분. 그리디 알고리즘 칸에서 들어갔지만
# 처음에 dp 인 줄 알고 어떻게 풀까 고민 조금 하다가, 그냥 습관처럼
# 알고리즘 탭을 봤더니 그리디, 그래프가 있어서 바로 dfs 로 풀었다.
# dp 라는 선입견을 가지니까 오히려 더 안풀릴 뻔 했다.
# 문제 자체는 그리디 특성답게, 생각만 나면 쉽다.
import sys
R, C = [int(x) for x in sys.stdin.readline().split()]
arr = [list(sys.stdin.readline().strip()) for _ in range(R)]
arr1=[[0 for x in range(C)] for _ in range(R)]
ans=0


def start(a,b):
    global ans
    if b==C-1:
        ans+=1
        return 1
    if a>0 and arr[a-1][b+1]=='.' and arr1[a-1][b+1]==0:
        arr1[a-1][b+1]=1
        if start(a-1,b+1):
            return 1
    if arr[a][b+1]=='.' and arr1[a][b+1]==0:
        arr1[a][b+1]=1
        if start(a,b+1):
            return 1
    if a<R-1 and arr[a+1][b+1]=='.' and arr1[a+1][b+1]==0:
        arr1[a+1][b+1]=1
        if start(a+1,b+1):
            return 1


for i in range(R):
    start(i,0)
print(ans)
