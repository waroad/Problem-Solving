# 1시간 정도, 구현에 dfs 문제인데 처음에 조금 헤매서 생각보다 오래걸렸다.
# 이게 도형들이 주어지면 그것들의 테두리를 따라가는 문제인데,
# 단순 2차원 배열로 색칠해서 풀면, ㄷ 자 모양으로 도형 3개가 겹쳐 있으면, 안쪽을 건너뛰고
# 바로 맞으편 도형을 테두리로 인식한다. 이를 해결하기 위해 2배율로 처음에 도형을
# 색칠해주면 되는데, 이거 조금 생각한다고 오래 걸렸다.


def solution(rectangle, characterX, characterY, itemX, itemY):
    arr=[[0 for _ in range(24)] for _ in range(24)]

    def color(a,b,c,d,e):
        if arr[a][b] == e:
            return
        arr[a][b]=e
        if a<c:
            color(a+1,b,c,d,e)
        if b<d:
            color(a,b+1,c,d,e)

    for ind, i in enumerate(rectangle):
        color(i[0]*2,i[1]*2,i[2]*2,i[3]*2,ind+1)
    ans=[]

    def find(a,b,c,d,e,pre_a,pre_b):
        if a==c and b == d:
            ans.append(e)
            return
        if a+1!=pre_a and arr[a+1][b] and (arr[a+1][b+1]==0 or arr[a][b+1]==0 or arr[a][b-1]==0 or
                               arr[a+1][b-1]==0 or arr[a+2][b]==0 or arr[a+2][b-1]==0 or arr[a+2][b+1]==0):
            find(a+1,b,c,d,e+1,a,b)
        if a-1!=pre_a and arr[a-1][b] and (arr[a-1][b+1]==0 or arr[a][b+1]==0 or arr[a][b-1]==0 or
                            arr[a-1][b-1]==0 or arr[a-2][b]==0 or arr[a-2][b-1]==0 or arr[a-2][b+1]==0):
            find(a - 1, b, c, d, e + 1,a,b)
        if b+1!=pre_b and arr[a][b+1] and (arr[a+1][b+1]==0 or arr[a+1][b]==0 or arr[a-1][b]==0 or
                               arr[a-1][b+1]==0 or arr[a][b+2]==0 or arr[a-1][b+2]==0 or arr[a+1][b+2]==0):
            find(a, b+1, c, d, e + 1,a,b)
        if b-1!=pre_b and arr[a][b-1] and (arr[a+1][b-1]==0 or arr[a+1][b]==0 or arr[a-1][b]==0 or
                               arr[a-1][b-1]==0 or arr[a][b-2]==0 or arr[a-1][b-2]==0 or arr[a+1][b-2]==0):
            find(a, b - 1, c, d, e + 1,a,b)

    find(characterX*2, characterY*2, itemX*2, itemY*2, 0,0,0)
    # arr.reverse()
    # for i in arr:
    #     print(i)
    # print(ans)
    return min(ans)//2


solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1)
