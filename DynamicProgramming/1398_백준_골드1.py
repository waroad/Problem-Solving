# 골드1, dp, 그리디, 30분 정도?
# 이제는 그냥 왠만한 dp 그리디는 골드 1도 무난하게 푸는 것 같다.
# 이것도 풀기도 전에 풀 수 있을 것 같아서 미리 github 에 올렸고
# 역시 쉽게 풀렸다.
# 아직 못푸는 게 비트마스킹이 접합된 dp 인데, 그것만 나중에 해봐야겠다.

import sys
T=int(input())
arr=[0]*100
for i in range(100):
    arr[i]=min(i%10+i//10,i%25+i//25)
    for j in range(1,4):
        if i>j*25:
            arr[i]=min(arr[i],j+(i-j*25)%10+(i-j*25)//10)
for i in range(T):
    tmp=int(sys.stdin.readline())
    ans=0
    while tmp>0:
        ans += (lambda x: arr[x % 100])(tmp)
        tmp//=100

    print(ans)
