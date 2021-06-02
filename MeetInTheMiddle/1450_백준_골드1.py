# meet in the middle, 냅색, 골드 1, 1시간 정도.
# 이거는 meet in the middle 존재를 모르고 그냥 풀다가, 감도 안잡혀서 블로그 좀 뒤지다가
# meet in the middle 이 먼지 보고, 그 글을 참고해서 풀었다.
# 내가 다 짜지는 않았지만, 그래도 하나 이해하고 간다는 느낌으로 했다.


def brute_force(l, w, arr, arrD):
    if l >= len(arr):
        if w<=c:
            arrD.append(w)
        return

    brute_force(l + 1, w, arr, arrD)
    brute_force(l + 1, w + arr[l], arr, arrD)


def lower_bound(start, end, key):
    global cnt
    while start < end:
        mid = (start + end) // 2
        if b_sum[mid] <= key:
            start = mid + 1
        else:
            end = mid
    return end


n, c = [int(x) for x in input().split()]
weight = [int(x) for x in input().split()]
cnt = 0

a_weight = weight[:n // 2]
b_weight = weight[n // 2:]
a_sum = []
b_sum = []
brute_force(0, 0,a_weight,a_sum)
brute_force(0, 0,b_weight,b_sum)
b_sum.sort()
for i in a_sum:
    cnt += (lower_bound(0, len(b_sum), c - i))
print(cnt)
