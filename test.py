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