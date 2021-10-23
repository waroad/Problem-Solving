# 골드 1, dp, 그리디, 트리 문제, 약 1시간. 세 개의 카테고리가 있긴 하지만 다 조금씩 들어가서 어렵진 않았다.
# 컨셉 자체는 잡는데 20분도 안걸렸다. 단방향 트리 형식으로 밑에 노드의 값들을 적절히 더해서
# 위의 노드를 구하는, 직관적인 dp 문제였다.
# 근데 컨셉을 잡고 재귀까지 다 짜고 난 다음에, 밑에 노드의 값들로 부모 노드를 구하는 과정에서
# 약간 잘못 생각해가지고 그걸로 30분 정도 버렸던 것 같다. 확실히 그리디, dp 문제가
# 생각만 나면 참 쉬운 문제인 것 같다.
# 추가- 다시 들어가보니 골드 1이었다. 그새 다운그레이드 된건가? 모르겠다.
N=int(input())
arr=[int(x) for x in input().split()]
arr1=[[] for _ in range(N)]  # 노드 별 자식을 저장하는 배열
dp=[0]*N


def find(a):
    tmp=[]
    if len(arr1[a])==0:  # 자식이 없을 경우 시행시간이 0 걸린다.
        return 0
    for i in range(len(arr1[a])):
        tmp.append(find(arr1[a][i]))
    tmp.sort(reverse=True)
    dp[a]=tmp[0]+1
    for j in range(1,len(tmp)):
        dp[a]=max(dp[a],tmp[j]+j+1)
    return dp[a]


for j in range(1,N):
    arr1[arr[j]].append(j)
find(0)
print(dp[0])
