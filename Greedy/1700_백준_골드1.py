# 골드1 , 그리디, 30분 좀 넘게
# 요즘 복잡한 코드를 짜기 귀찮아서 그리디만 푸는데
# 이것도 도움이 되는지 모르겠다. 그래프랑 dp도 다시 해야하는데
# 확실히 그리디가 동 난이도 대비 쉬운 것 같다.
n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
arr_n= {}
ans=0
for ind, i in enumerate(arr):
    if len(arr_n)<n:
        arr_n[i]=0
    else:
        if i not in arr_n:
            ind+=1
            cnt=1
            for ar in arr_n:
                arr_n[ar]=0
            arr_n[i] = 1
            while ind<k and cnt<n:
                if arr[ind] in arr_n and arr_n[arr[ind]]==0:
                    arr_n[arr[ind]]=1
                    cnt+=1
                ind+=1
            for ar in arr_n:
                if arr_n[ar]==0:
                    del arr_n[ar]
                    ans+=1
                    break

print(ans)
