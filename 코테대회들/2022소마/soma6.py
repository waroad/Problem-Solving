N,M=[int(x) for x in input().split()]
arr=[[] for _ in range(N)]
arr_t=[0]*N
for k in range(N-1):
    tmp=[int(x) for x in input().split()]
    arr[tmp[0]-1].append([tmp[1]-1,tmp[2]])
    arr[tmp[1]-1].append([tmp[0]-1,tmp[2]])

for k in range(M):
    tmp=[int(x) for x in input().split()]
    arr_t[tmp[0]-1]=tmp[1]
ans=0
node=-1


def begin(index,par,cost):
    global ans,node
    for i in arr[index]:
        if i[0]!=par:
            cost+=i[1]
            if arr_t[i[0]]-cost*2>ans:
                ans=arr_t[i[0]]-cost*2
                node=i[0]+1
            elif arr_t[i[0]]-cost*2==ans and i[0]<node:
                node=i[0]+1

            begin(i[0],index,cost)
            cost-=i[1]


begin(0,-1,0)
print(node, ans)