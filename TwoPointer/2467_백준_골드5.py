# 골드 5, 투 포인터 문제.
# 매우 쉬웠다.

N=int(input())
arr=[int(x) for x in input().split()]
ans=10000000000
S=0
E=N-1
arr2=[]
while S<E:
    tmp=arr[S]+arr[E]
    if abs(tmp)<ans:
        arr2=[arr[S],arr[E]]
        ans=abs(tmp)
    if tmp>0:
        E-=1
    else:
        S+=1

print(*arr2)
