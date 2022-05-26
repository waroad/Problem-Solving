import itertools
import sys
sys.setrecursionlimit(10**6)
with open("input.txt", "r") as f:
    N=int(f.readline())
    arr2 = [[float(x) for x in f.readline().split()] for _ in range(N)]
arr=[[0 for _ in range(N)] for _ in range(N)]
for ind1,i in enumerate(arr2):
    for ind2,j in enumerate(arr2):
        arr[ind1][ind2]=((i[0]-j[0])**2 + (i[1]-j[1])**2)**0.5

vis=[[1000000000 for _ in range(2**N)] for _ in range(N)]
path=[[[0] for _ in range(2**N)] for _ in range(N)]
comb=[i for i in range(1,N)]
for i in range(N):
    vis[i][2**i+1]=arr[0][i]
    path[i][2**i+1].append(i)
for i in range(2,N):
    tmp=list(itertools.combinations(comb, i))
    for k in tmp:
        tt=sum(2**p for p in k)+1
        for j in k:
            min_t=1000000000
            tmp2=[]
            for l in k:
                if l!=j and arr[l][j] and min_t>vis[l][tt-2**j]+arr[l][j]:
                    min_t=vis[l][tt-2**j]+arr[l][j]
                    tmp2=path[l][tt-2**j][:]
            tmp2.append(j)
            vis[j][tt]=min_t
            path[j][tt]=tmp2


ans=1000000000
path_ans=[]
for i in range(N):
    if arr[i][0]:
        ans1=ans
        ans=min(ans,vis[i][2**N-1]+arr[i][0])
        if ans1!=ans:
            path_ans=path[i][2**N-1][:]
            path_ans.append(0)
ans=round(ans, 2)
path_ans1=''.join(str(a)+"," for a in path_ans)
path_ans1=path_ans1[0:-1]
f = open("output.txt", 'w')
f.write(str(ans)+"\n")
f.write(path_ans1)
f.close()
