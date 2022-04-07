
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
                if len(arr2[i][0])==0:
                    find(i)
                arr2[a][0] = arr2[a][0] | arr2[i][0]
                arr2[a][0].add(i)

    def find2(a):
        for i in range(1,n+1):
            if arr[a][i] == -1:
                if len(arr2[i][1])==0:
                    find2(i)
                arr2[a][1]=arr2[a][1] | arr2[i][1]
                arr2[a][1].add(i)

    for i in range(1,n+1):
        if len(arr2[i][0])==0:
            find(i)
        if len(arr2[i][1])==0:
            find2(i)
    for i in range(1,n+1):
        if len(arr2[i][0])+len(arr2[i][1])== n-1:
            ans+=1
    # print(arr2)
    # print(ans)
    return ans


solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])