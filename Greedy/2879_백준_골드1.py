# 골드 1, 그리디, 30분
# 지금은 시험기간이라 그냥 그리디만 계속 풀려고 한다. 앞으로 한 10일 남았다.
# 이것도 논리적으로 생각해서 사실 순서가 상관없다는 것을 깨닫기만 하면
# 하면 풀 수 있는 그런 문제였다. 딱히 테크닉 이런 것도 없다.

n=int(input())
arr_t=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
arr=[arr[i]-arr_t[i] for i in range(n)]

ind=0
ans=0
while ind<n:
    if arr[ind]==0:
        ind+=1
        continue
    elif arr[ind]<0:
        cur=ind+1
        max_t=arr[ind]
        while cur<n and arr[cur]<0:
            if arr[cur]>max_t:
                max_t=arr[cur]
            cur+=1
        for i in range(ind,cur):
            arr[i]-=max_t
        max_t*=-1
    else:
        cur = ind + 1
        max_t = arr[ind]
        while cur < n and arr[cur] > 0:
            if arr[cur] < max_t:
                max_t = arr[cur]
            cur += 1
        for i in range(ind, cur):
            arr[i] -= max_t

    ans+=max_t

print(ans)
