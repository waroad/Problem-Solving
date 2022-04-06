
def solution(n, results):
    arr=[[0 for _ in range(n+1)] for _ in range(n+1)]
    arr2=[[set() for _ in range(2)] for _ in range(n+1)]
    ans=0
    for i in results:
        arr[i[0]][i[1]]=-1
        arr[i[1]][i[0]]=1

    def find(a):
        for i in range(1,n+1):
            if arr[a][i]==1:
                if len(arr2[i][0]):
                    up.union(arr2[i][0])
                else:
                    find(i)
                    arr2[i][0]=up
                    up.add(i)

    def find2(a):
        for i in range(1,n+1):
            if arr[a][i]==-1:
                if len(arr2[i][1]):
                    down.union(arr2[i][1])
                else:
                    find(i)
                    arr2[i][1]=down
                    down.add(i)

    for i in range(1,n+1):
        up=set([])
        down=set([])
        find(i)
        find2(i)
        if len(up)+len(down)==n-1:
            ans+=1
        arr2[i][0]=up
        arr2[i][1]=down
        print(arr2)
    return ans


solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])