m, n = [int(x) for x in input().split()]
arr= [[int(x) for x in input().split()] for _ in range(m)]


def check(a,b):  # 자기 주위에 몇개의 생명체가 있는지 세는 함수. 주위 좌표를 다 확인한다.
    cnt=0
    if a>0 and arr[a-1][b]==1:
        cnt+=1
    if b>0 and arr[a][b-1]==1:
        cnt+=1
    if b>0 and a>0 and arr[a-1][b-1]==1:
        cnt+=1
    if a+1<m and arr[a+1][b]==1:
        cnt+=1
    if b+1<m and arr[a][b+1]==1:
        cnt+=1
    if a+1<m and b + 1 < m and arr[a+1][b + 1] == 1:
        cnt += 1
    if a+1<m and b>0 and arr[a+1][b-1]==1:
        cnt +=1
    if b+1<m and a>0 and arr[a-1][b+1]==1:
        cnt +=1
    return cnt


# 다음 세대 만드는 함수. 배열 안의 모든 좌표에 대해, 주위 생명체의 수를 세어서 그걸 바탕으로 다음 세대 배열인 arr2를 만들고
# 그 배열을 return 하여, 다시 현재 세대를 업데이트한다.
def next_gen():
    arr2= [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result=check(i,j)
            if arr[i][j] and 1<result<4:
                arr2[i][j]=1
            elif result==3:
                arr2[i][j]=1
    return arr2


# n 번만큼 시뮬레이트 한다.
for i in range(n):
    arr2=next_gen()
    arr=[x[:] for x in arr2]

# 출력
for i in arr:
    print(*i,sep='')