N=int(input())
arr=[input() for x in range(N)]
arr.sort()
T=int(input())
for i in range(T):
    tmp=input()
    cnt=0
    for k in arr:
        if tmp in k:
            cnt+=1
    print(cnt)