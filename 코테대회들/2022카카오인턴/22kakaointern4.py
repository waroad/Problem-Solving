import sys
import random

limit_number = 1000000
sys.setrecursionlimit(limit_number)

ans = [-1, 1000000000]


def solution(n, paths, gates, summits):
    global ans
    arr = [{} for _ in range(n)]
    random.shuffle(paths)
    gates = {gates[i] - 1:0 for i in range(len(gates))}
    summits = {summits[i] - 1: 0 for i in range(len(summits))}
    for i in paths:
        if i[1]-1 not in gates and i[0] - 1 not in summits:
            arr[i[0] - 1][i[1] - 1]= i[2]
        if i[0]-1 not in gates and i[1] - 1 not in summits:
            arr[i[1] - 1][i[0] - 1]= i[2]
    dp = [10000000] * n

    def find(a, b):
        global ans
        for i in arr[a]:
            if i in summits:
                B = b
                if arr[a][i]>B:
                    B=arr[a][i]
                if B < ans[1] or (B == ans[1] and i < ans[0]):
                    ans = [i, B]
                    if B == b:
                        return
                continue
            if dp[i] <= b or dp[i] <= arr[a][i]:
                continue
            B = b
            if arr[a][i] > B:
                B = arr[a][i]
            if dp[i] > B and ans[1] >= B:
                dp[i] = B
                find(i, B)

    for i in gates:
        find(i, 0)
    ans[0] += 1
    return ans
