# 골드 1, dp, 1시간 반 정도
# 컨셉을 한번 잘못 잡아서 오래 걸렸다.
# 그냥 for 구문으로 하면 될 것을 큐로 하려고 하니까 시간이 너무 오래 걸렸는데,
# 이게 파이썬이 원래 느려서 이런건지 의심하느라 코드를 안버리고 조금씩 수정만 하다가
# 확실히 이 방법은 느리구나라는 것을 깨닫기 까지가 오래걸렸다. 그 다음에 짜는거는
# 얼마 안걸렸다. 유형은 전에 카카오 기출 중에 비슷한 것을 풀어봐서 괜찮았고
# dp 도 생각보다는 할만하다는 생각이 들었다.

import sys
n, m = [int(x) for x in input().split()]
arr = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
arr2 = [[[0, 0] for _ in range(m)] for _ in range(n)]
arr2[0][0][0] = arr[0][0]
arr2[0][0][1] = arr[0][0]
for i in range(1,m):
    arr2[0][i][0]=arr[0][i]+arr2[0][i-1][0]
    arr2[0][i][1]=arr[0][i]+arr2[0][i-1][0]
for i in range(1,n):
    arr2[i][0][0]=arr2[i-1][0][1]+arr[i][0]
    arr2[i][m-1][1]=arr2[i-1][m-1][0]+arr[i][m-1]
    for j in range(1,m):
        arr2[i][j][0]=max(max(arr2[i-1][j][0],arr2[i-1][j][1]),arr2[i][j-1][0])+arr[i][j]
        arr2[i][m-1-j][1]=max(max(arr2[i-1][m-1-j][1],arr2[i-1][m-1-j][0]),arr2[i][m-j][1])+arr[i][m-1-j]

print(arr2[n - 1][m - 1][0])
