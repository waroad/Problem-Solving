# 골드 5, 기하학, 20분
# 그냥 오늘은 풀기 싫어서 쉬운거 하나 풀었다.
# 다각형의 넓이를 어떻게 구하는지 수학 식을 알기만 하면 바로 풀 수 있는 문제이다.
# 그걸 몰랐기에 구글링하고, 바로 구현하였다.
n=int(input())
ans=0
arr=[[int(x) for x in input().split()] for _ in range(n)]
for i in range(n):
    ans+=arr[i][0]*arr[i-1][1]-arr[i][1]*arr[i-1][0]
print(abs(ans/2))
