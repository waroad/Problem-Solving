import itertools
N=int(input())
arr=[int(x) for x in input().split()]
k=itertools.combinations(arr, 3)
cnt=0
for t in k:
    if 2000<=sum(t)<=2500:
        cnt+=1
print(cnt)