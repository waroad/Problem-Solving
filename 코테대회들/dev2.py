from itertools import product
import sys
sys.setrecursionlimit(20000000)


def solution(grid):
    answer=0

    def find2(a,b, tt):
        arr[a][b]='d'
        if a+1<len(grid) and tt==arr[a+1][b]:
            find2(a+1,b,tt)
        if a > 0 and tt == arr[a - 1][b]:
            find2(a - 1, b, tt)
        if b+1<len(grid[0]) and tt==arr[a][b+1]:
            find2(a,b+1, tt)
        if b>0 < len(grid[0]) and tt == arr[a][b-1]:
            find2(a, b-1, tt)

    def find():
        dict1=[]
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if arr[a][b]!='d' and arr[a][b] not in dict1:
                    dict1.append(arr[a][b])
                    tt=arr[a][b]
                    find2(a,b,tt)
                elif arr[a][b]!='d' and arr[a][b] in dict1:
                    return -1
        return 0

    arr=[]
    qq=[]
    abc=['a','b','c']
    for i in range(len(grid)):
        tmp=[]
        for j in range(len(grid[0])):
            tmp.append(grid[i][j])
        arr.append(tmp)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if arr[i][j]=='?':
                qq.append([i,j])
    data = product(abc, repeat=len(qq))
    b = [x[:] for x in arr]
    for i in data:
        for ind, j in enumerate(i):
            arr[qq[ind][0]][qq[ind][1]]=j
        if find()==0:
            answer+=1
        arr = [x[:] for x in b]
    return answer




print(solution(["aa?"]))