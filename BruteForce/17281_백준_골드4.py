# 골드 4, 브루트포스, 2시간?
# 사실 문제 자체는 쉬운 문제다. 그런데 파이썬을 지원하지 않는
# 삼성 문제의 특성 때문에, 그걸 파이썬으로 억지로 통과하게 한다고 시간이 오래 걸렸다.
# pypy3 로 짰는데, 진짜 말도 안되는거 하나에서 시간초과가 걸렸다.
# int 3 개를 배열에 넣어서 비교했는데, 그거를 배열에서 빼고 변수 3개로 하니까
# 바로 통과했다. 참 파이썬이 느리긴 느린 것 같다.
from itertools import permutations
n=int(input())
arr=[[int(x) for x in input().split()] for _ in range(n)]
ans=0
ent1=permutations(range(1,9), 8)


def count():
    j = 0
    score=0
    for i in range(0,n):
        out=0
        base1,base2,base3=0,0,0
        while out<3:
            if arr[i][ent[j]] == 0:
                out += 1
            elif arr[i][ent[j]] == 1:
                score+=base3
                base3=base2
                base2=base1
                base1=1
            elif arr[i][ent[j]] == 2:
                score += base3+base2
                base3 = base1
                base2 = 1
                base1=0
            elif arr[i][ent[j]] == 3:
                score += base3+base2+base1
                base3 = 1
                base2 = 0
                base1=0
            else:
                score +=base3+base2+base1+1
                base3 = 0
                base2 = 0
                base1=0
            j = (j+1)%9

    return score


for ent in ent1:
    ent=[*ent[:3],0,*ent[3:]]
    tmp=count()
    if tmp>ans:
        ans=tmp
print(ans)


