# 골드 4, 그래프, DFS, 50분 가량.
# 근래 또 3일 씩 두번 비어있는데 가족 여행을 두번 갔다왔다.
# 이것도 UCPC 기출인데, 골드4라 조금 무시했는데 쉽진 않았다.
# len(arr)을 쓰는 것도, 좋지 않은 습관이란 것을 알고는 있었는데, 이번에 처음으로 이것 때문에
# 통과 못한 것이 바꾸니까 바로 통과한 사례가 나왔다. len(arr[a])를 싹 다 arrL[a]로 바꾸어
# 주었더니 통과했다. 푼 방법은 그냥 모든 좌표 별 루트에서부터의 길이를 구하고, 이제 각 좌표 별로
# 끝 사거리까지와의 거리를 구해서 다시 루트부터 내려와서 거리를 다 더해줬다. 

import sys
sys.setrecursionlimit(150000)
n, s, d=[int(x) for x in input().split()]
arr=[[] for i in range(n)]
arrL=[0]*n
arrD=[0]*n
arrD2=[0]*n


def loop(a,b,c):
    for i in range(arrL[a]):
        if arr[a][i]!=b:
            arrD[arr[a][i]]=c+1
            loop(arr[a][i],a,c+1)


def loop2(a,b):
    max_t=0
    for i in range(arrL[a]):
        if arr[a][i]!=b:
            tmp=loop2(arr[a][i],a)
            if tmp>max_t:
                max_t=tmp

    arrD2[a]=max(max_t,arrD[a])-arrD[a]
    return max(max_t,arrD[a])


def loop3(a,b):
    global ans
    ans+=1
    for i in range(arrL[a]):
        if arr[a][i]!=b:
            if arrD2[arr[a][i]]>=d:
                loop3(arr[a][i],a)

    ans+=1


for i in range(n-1):
    temp=[int(x) for x in sys.stdin.readline().split()]
    arr[temp[0]-1].append(temp[1]-1)
    arr[temp[1]-1].append(temp[0]-1)
    arrL[temp[0]-1]+=1
    arrL[temp[1]-1]+=1

loop(s-1,-1,0)
loop2(s-1,-1)
# print(arr)
# print(arrL)
# print(arrD)
# print(arrD2)
ans=-2
loop3(s-1,-1)
print(ans)





