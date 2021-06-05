# 골드 2, 그리디, dp 문제, 약 1시간 정도 걸렸다.
# 처음에 바로 아이디어가 생각나진 않았고, 한쪽 방향으로만 막대기를 움직일 수 있게
# 짜야지 하고 생각이 나고 풀었는데, 9프로에서 틀려서
# 랜덤 테스트케이스 생성기를 만든 다음 정답 코드의 값과 비교해가면서 풀었다.
# 솔직히 아직도 그리디가 뭔지 잘 모르겠다.

n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr1=[0]*(n+1)  # 들어온 배열의 덧셈, 즉 index 두 개 알았을 때 그 index 사이의 값의 합 구하기 위한 배열
arr2=[0]*(m+1)  # 나누고 있는 칸막이와 양 끝 index
arr2[m]=n
arr3=[0]*m  # 실제로 계산한 각 칸 마다 있는 공들 수의 합
arr4=[0]*m  # 정답을 출력하기 위한, 전체 칸 중 최대 무게의 칸의 값이 최솟값일 때의 배열 저장
max=0
max_in=0
for i in range(n):
    arr1[i+1]=arr[i]+arr1[i]
for i in range(m-1,0,-1):
    arr2[i]=arr2[i+1]-1
for j in range(m):
    arr3[j]=arr1[arr2[j+1]]-arr1[arr2[j]]
    if arr3[j]>max:
        max_in=j
        max=arr3[j]
for j in range(m):
    arr4[j]=arr2[j+1]-arr2[j]
ans=max
while max_in!=m-1:
    arr2[max_in+1]-=1
    max=0
    for j in range(m):
        arr3[j] = arr1[arr2[j + 1]] - arr1[arr2[j]]
        if arr3[j] >= max:
            max_in = j
            max = arr3[j]
    if max<ans:
        ans=max
        for j in range(m):
            arr4[j]=arr2[j+1]-arr2[j]
    if max_in==m-1: break
print(ans)
print(*arr4)
