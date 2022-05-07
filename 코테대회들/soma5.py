import bisect
arr=[int(x) for x in input().split()]
arr.sort()
k=int(input())
for i in range(k):
    tmp=[int(x) for x in input().split()]
    for t in tmp:
        bisect.insort(arr, t)
    print(arr[int(len(arr)//3)],arr[int(len(arr)*2//3)])