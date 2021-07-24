import sys, copy

n= int(input())

ing=[[[0 for x in range(4)] for y in range(4)] for z in range(n*4)]
ing2=[[['0' for _ in range(4)] for _ in range(4)] for _ in range(n*4)]
arr=[[0 for _ in range(5)] for _ in range(5)]
arr2=[[0 for _ in range(5)] for _ in range(5)]
arr3=[[0 for _ in range(5)] for _ in range(5)]
arr4=[[0 for _ in range(5)] for _ in range(5)]
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


def score():
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
    # if arr_sel[0] == 1 and arr_sel[1] == 2 and arr_sel[2] == 0 and arr2[0][4]==0 and arr2[4][3]=='G' and arr2[1][4]=='G':
    #     for i in range(5):
    #         print(arr[i])
    #     for i in range(5):
    #         print(arr2[i])
    #     print("")
    #     print(tmp)
    if tmp>ans:

        ans=tmp


def brute(a,x,y):
    # for i in range(4):
    #     for j in range(4):
    #         arr3[i+x][j+y]=arr[i+x][j+y]
    #         arr4[i+x][j+y]=arr2[i+x][j+y]
    for i in range(4):
        for j in range(4):
            arr[i+x][j+y]+=ing[a][i][j]
            if arr[i+x][j+y]<0: arr[i+x][j+y]=0
            if arr[i+x][j+y]>9: arr[i+x][j+y]=9
            if ing2[a][i][j]!='W':
                arr2[i+x][j+y]=ing2[a][i][j]
    # for i in range(4):
    #     for j in range(4):
    #         arr[i+x][j+y]=arr3[i+x][j+y]
    #         arr2[i+x][j+y]=arr4[i+x][j+y]


def do(count):
    global arr, arr2
    if count==3:
        score()
    else:
        for i in range(2):
            for j in range(2):
                arr3 = copy.deepcopy(arr)
                arr4 = copy.deepcopy(arr2)
                for k in range(4):

                    brute(k+arr_sel[count]*4,i,j)
                    do(count+1)
                    for m in range(4):
                        for l in range(4):
                            arr[i + m][j + l] = arr3[i + m][j + l]
                            arr2[i + m][j + l] = arr4[i + m][j + l]


def choose():
    for i in range(n):
        if i not in arr_sel:
            arr_sel.append(i)
            if len(arr_sel)==3:
                do(0)
            else:
                choose()
            arr_sel.pop()


choose()
# for i in range(n*4):
#     for j in range(4):
#         print(ing[i][j])
#     print("")
#     for j in range(4):
#         print(ing2[i][j])
#     print("")
#     print("")
#
# for i in range(5):
#     print(arr[i])
# for i in range(5):
#     print(arr2[i])
# print(ans)
print(ans)
