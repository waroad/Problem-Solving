# 그래프와 dp, 3단계임에도 불구하고 1시간 조금 넘게 걸린 것 같다.
# 처음에는 이게 승자, 패자를 알려주고 순위를 맞추는 것이기에
# 위상정렬인줄 알고 그렇게 접근했는데,
# 아무리 해도 안돼서 결국 그래프 쪽으로 넘어왔고, 그냥 그래프로 하니까
# 시간초과가 떠서 dp로 조금 응용해서 결국 풀었다. 프로그래머스 3단계 중에는
# 좀 어려운 편인 것 같다.
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