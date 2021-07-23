# 골드3, 브루트포스, 40분 가량
# 이것도 UCPC 문제인데, 오랫만에 바로 맞췄다.
# 브루트포스로 박스 세개를 담을 수 있는 직사각형의 최소 넓이를 구하는 것인데,
# 가능한 모든 경우의 수를 어떻게 구할지를 생각하면 되는 문제다. 역시 UCPC는 어렵다.

import sys
n=int(input())


def find(s1,s2,s3):
    global ans
    if s2[1]<=s1[1] and s2[0]>=s3[0]:
        tmp=(s1[0]+s2[0])*max(s2[1]+s3[1],s1[1])
    elif s1[1]<=s2[1] and s1[0]>=s3[0]:
        tmp=(s1[0]+s2[0])*max(s1[1]+s3[1],s2[1])
    else:
        tmp=max(s1[0]+s2[0],s3[0])*(max(s1[1],s2[1])+s3[1])
    tmp2=max(s1[0],s2[0],s3[0])*(s1[1]+s2[1]+s3[1])
    if tmp<ans:
        ans=tmp
    if tmp2<ans:
        ans=tmp2


for i in range(n):
    ans=1000000000
    s1= [int(x) for x in sys.stdin.readline().split()]
    s2= [int(x) for x in sys.stdin.readline().split()]
    s3= [int(x) for x in sys.stdin.readline().split()]
    for j in range(2):
        for k in range(2):
            for l in range(2):
                find([s1[j],s1[(j+1)%2]],[s2[k],s2[(k+1)%2]],[s3[l],s3[(l+1)%2]])
                find([s1[j],s1[(j+1)%2]],[s3[l],s3[(l+1)%2]],[s2[k],s2[(k+1)%2]])
                find([s2[k],s2[(k+1)%2]],[s1[j],s1[(j+1)%2]],[s3[l],s3[(l+1)%2]])
                find([s2[k],s2[(k+1)%2]],[s3[l],s3[(l+1)%2]],[s1[j],s1[(j+1)%2]])
                find([s3[l],s3[(l+1)%2]],[s1[j],s1[(j+1)%2]],[s2[k],s2[(k+1)%2]])
                find([s3[l],s3[(l+1)%2]],[s2[k],s2[(k+1)%2]],[s1[j],s1[(j+1)%2]])
    print(ans)
