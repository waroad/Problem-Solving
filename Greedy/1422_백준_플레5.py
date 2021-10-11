# 플레5, 그리디, 20분
# 16496과 매우 비슷하다. 그래서 딱히 할 말도 없다.
n,k=[int(x) for x in input().split()]
arr_t=[int(input()) for x in range(n)]
arr=[list(str(x)) for x in arr_t]
arr2=[]
for _ in range(k-n):
    arr.append(list(str(max(arr_t))))
for ind,i in enumerate(arr):
    tmp=(lambda x: x*10)(i)
    # for j in range(10):
    #     tmp.extend(i)
    tmp=tmp[:10]
    tmp.append(ind)
    arr2.append(tmp)
arr2.sort(reverse=True)
ans=[]
for i in range(len(arr)):
    ans.extend(arr[arr2[i][10]])
print(int(''.join(ans)))
