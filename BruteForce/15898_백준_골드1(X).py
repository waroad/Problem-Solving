# 골드1, 브루트포스 및 구현, 1시간 반 가량
# 브루트포스로 2차원 배열을 계속 수정하는데, 이전 상태를 가지고 있다가 다시 되돌려가며
# 깊이 우선으로 풀어야 하는 문제다. 처음에 deepcopy로 2차원 배열을 저장했었는데,
# 너무 느린 것 같아서 list slicing으로 바꾸었다. 그래도 시간초과가 나서, 맞게 짠 것 같은데
# 뭐가 문제지 하고 맞은 사람을 보니, 파이썬이랑 pypy3는 정답자가 없었다.
# pypy3로는 맞출 수 없는 문제인가 싶다.

n= int(input())

ing=[[[0 for x in range(4)] for y in range(4)] for z in range(n*4)]
ing2=[[['0' for _ in range(4)] for _ in range(4)] for _ in range(n*4)]
arr=[[0 for _ in range(5)] for _ in range(5)]
arr2=[[0 for _ in range(5)] for _ in range(5)]
arr_sel=[]
ans=0
for i in range(0,n*4,4):
    for j in range(4):
        tmp = [int(x) for x in input().split()]
        ing[i][j] = tmp
    for k in range(1,4):
        for j in range(4):
            for l in range(4):
                ing[i+k][j][l]=ing[i+k-1][l][3-j]
    for j in range(4):
        tmp = [x for x in input().split()]
        ing2[i][j] = tmp
    for k in range(1, 4):
        for j in range(4):
            for l in range(4):
                ing2[i + k][j][l] = ing2[i + k - 1][l][3 - j]


def cnt_score():
    global ans
    tmp=0
    for i in range(5):
        for j in range(5):
            if arr2[i][j]=='R':
                tmp+=arr[i][j]*7
            elif arr2[i][j]=='B':
                tmp+=arr[i][j]*5
            elif arr2[i][j]=='G':
                tmp+=arr[i][j]*3
            elif arr2[i][j]=='Y':
                tmp+=arr[i][j]*2
    if tmp>ans:
        ans=tmp


def copy_arr(a,x,y):
    for i in range(4):
        for j in range(4):
            arr[i+x][j+y]+=ing[a][i][j]
            if arr[i+x][j+y]<0: arr[i+x][j+y]=0
            elif arr[i+x][j+y]>9: arr[i+x][j+y]=9
            if ing2[a][i][j]!='W':
                arr2[i+x][j+y]=ing2[a][i][j]


def brute(count):
    global arr, arr2
    if count==3:
        cnt_score()
    else:
        arr3 = [[] for _ in range(5)]
        arr4 = [[] for _ in range(5)]
        for m in range(5):
                arr3[m]=arr[m][:]
                arr4[m]=arr2[m][:]
        for i in range(2):
            for j in range(2):
                for k in range(4):
                    copy_arr(k+arr_sel[count]*4,i,j)
                    brute(count+1)
                    for m in range(4):
                        arr[i + m] = arr3[i + m][:]
                        arr2[i + m] = arr4[i + m][:]


def choose():
    for i in range(n):
        if i not in arr_sel:
            arr_sel.append(i)
            if len(arr_sel)==3:
                brute(0)
            else:
                choose()
            arr_sel.pop()


choose()
print(ans)
