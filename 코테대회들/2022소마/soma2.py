N,Q=[int(x) for x in input().split()]
l_size=[int(x) for x in input().split()]
r_size=[0]*(N)
arr=[[] for _ in range(N)]
for i in range(Q):
    tmp=[x for x in input().split()]
    if tmp[0]=='I':
        r_size[0]+=int(tmp[2])
        arr[0].append([tmp[1],int(tmp[2])])
        for k in range(N-1):
            if r_size[k]>l_size[k]:
                r_size[k]=0
                for j in arr[k]:
                    t=0
                    for l in arr[k+1]:
                        if j[0]==l[0]:
                            r_size[k+1]+=j[1]-l[1]
                            l[1]=j[1]
                            t=1
                            break
                    if t==0:
                        arr[k+1].append(j)
                        r_size[k + 1] += j[1]
                arr[k]=[]
    else:
        bb=0
        for k in range(N):
            if bb: break
            for j in arr[k]:
                if tmp[1]==j[0]:
                    print(k+1,j[1])
                    bb=1
                    break
        if bb==0:
            print('none')
