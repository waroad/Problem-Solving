def solution(n, edges, kk, a, b):

    def recurse(tt):
        if tt == b:
            if len(used2)<=kk*2:
                for key in used2:
                    needed[key]=0
            else:
                return
        if len(used2)>kk*2:
            return
        for i in arr[tt]:
            if i not in used:
                used[i]=0
                used2[str(tt)+str(i)]=0
                used2[str(i)+str(tt)]=0
                recurse(i)
                used2.pop(str(i)+str(tt))
                used2.pop(str(tt)+str(i))
                used.pop(i)

    arr=[[] for _ in range(n)]
    for edge in edges:
        arr[edge[0]].append(edge[1])
        arr[edge[1]].append(edge[0])

    needed={}
    used= {a:0}
    used2= {}

    recurse(a)
    return len(needed)//2


solution(8,[[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]],18,0,3)