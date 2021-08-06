# 플레 3, 그리디, 2시간?
# UCPC 2021 예선에서 나온 문제이다. 그 때 한 1시간 반 정도 아무리생각해도
# 못 풀었던 문제이다. 그래서 뭔가 테크닉이 더 있나보다 하고 있었는데
# 나중에 백준에 올라오고 보니 그냥 그리디였다. 그걸 감안해도 생각이 안나서
# 풀이를 봤더니 너무 아쉽다. 같은 색깔의 돌이 연속일 때 똑같은 색은 최댓값만
# 남기고 버리고, 맨 앞, 맨 뒤 돌은 버리는 것 까진 했는데 여기서 구하는 돌의 개수가
# 항상 남은 돌의 절반이라는 이 당연한 사실을 생각을 못해냈었다.
# 이건 진짜 테크닉이 아니라 머리싸움 인 것 같다. 내 힘으로 못푼게 약간 아쉽다.
n=int(input())
str=input()
arr=[int(x) for x in input().split()]
arr2=[]
tmp=arr[0]
for i in range(n-1):
    if str[i]==str[i+1]:
        tmp=max(tmp,arr[i+1])
    else:
        arr2.append(tmp)
        tmp=arr[i+1]
if len(arr2):
    arr2.pop(0)
ans=0
arr2.sort(reverse=True)
for i in range((len(arr2)+1)//2):
    ans+=arr2[i]
print(ans)
