def solution(N, number):
    arr=[[] for _ in range(8)]
    arr[0].append(N)
    for i in range(1,4):
        for j in arr[i-1]:
            arr[i].append(j*N)
            arr[i].append(j+N)
            if j//N==j/N:
                arr[i].append(j//N)
            if j-N > 0:
                arr[i].append(j-N)
    print(arr)


solution(5, 12)