# 골드 2, 플로이드 와샬, brutal force, 30분
# 처음에 이게 왜 플로이드 와샬이고 비트마스킹인지 이해가 안되서 갈피를 못잡다가
# input range가 10밖에 안돼서 그냥 brutal force로 하면 되겠다 해서 풀었더니
# 값이 이상해서 배열을 한 번 플로이드 와샬로 해주고 나니 답이 맞았다.

from itertools import permutations
n,s=[int(x) for x in input().split()]
arr=[[int(x) for x in input().split()] for _ in range(n)]
arr1=[]
for i in range(n):
    if i!=s: arr1.append(i)
ans=100000000
ent1=permutations(arr1)
for i in range(n):
    for j in range(n):
        for k in range(n):
            arr[j][k]=min(arr[j][k],arr[j][i]+arr[i][k])
for ent in ent1:
    tmp_ans=arr[s][ent[0]]
    for i in range(len(ent)-1):
        tmp_ans+=arr[ent[i]][ent[i+1]]
    if tmp_ans<ans: ans=tmp_ans

print(ans)
