# 골드 4, 그리디, 20분
# UCPC 이제 풀 수 있는 문제도 거의 없고, (남은 UCPC 기출은 골1 혹은 이상인데, 얘네는
# 체감상 더 어렵기에 풀기 어렵다.) 그래서 그냥 오랫만에 환기할 겸
# 쉬운 그리디 풀었다. 그냥 좀 생각하면 풀리는 문제이다. 이런 쉬운 문제만
# 있었으면 좋았을 텐데.

n=int(input())
arr2=[0]*10
exist=[]
for i in range(n):
    tmp=[x for x in input()]
    for j in range(len(tmp)):
        tmp1=1
        for k in range(len(exist)):
            if tmp[j]==exist[k]:
                arr2[k]+=10**(len(tmp)-j-1)
                tmp1=0
                break
        if tmp1==1:
            exist.append(tmp[j])
            arr2[len(exist)-1]+=10**(len(tmp)-j-1)
ans=0

arr2.sort(reverse=True)
for i in range(10):
    ans+=arr2[i]*(9-i)
print(ans)
