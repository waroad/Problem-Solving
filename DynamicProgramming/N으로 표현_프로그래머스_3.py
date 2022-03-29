# 쌩 dp 고 30분 좀 넘게 걸렸다.
# 그냥저냥 dp로 구현 좀 하면 된다.
# 지금 코드를 보면, 중복된 값도 list 에 넣는 매우 비효율적인 방법인데,
# 이걸 dict 로 바꾸면 조금 더 효율적이게 바꿀 수 있겠지만 이대로도 통과여서
# 그냥 이대로 넣었다.
def solution(N, number):
    arr=[[] for _ in range(8)]
    arr[0].append(N)
    if N==number:
        return 1
    for i in range(1,8):
        for k in range(i):
            for j in range(len(arr[i-k-1])):
                for m in range(len(arr[k])):
                    if arr[i-k-1][j]*arr[k][m]==number:
                        return i+1
                    if arr[i-k-1][j]+arr[k][m]==number:
                        return i+1
                    if arr[i-k-1][j]/arr[k][m]==number:
                        return i+1
                    if arr[i-k-1][j]-arr[k][m]==number:
                        return i+1
                    if int(str(N)*(i+1))==number:
                        return i+1
                    arr[i].append( int(str(N)*(i+1)))
                    arr[i].append(arr[i-k-1][j]*arr[k][m])
                    arr[i].append(arr[i-k-1][j]+arr[k][m])
                    if (arr[i-k-1][j]//arr[k][m])==(arr[i-k-1][j]/arr[k][m]):
                        arr[i].append(arr[i-k-1][j]//arr[k][m])
                    if (arr[i-k-1][j]-arr[k][m])> 0:
                        arr[i].append(arr[i-k-1][j]-arr[k][m])
    return -1

solution(2, 11)