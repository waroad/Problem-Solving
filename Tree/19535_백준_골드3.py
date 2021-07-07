# 골드 3, 트리, 약 30분
# UCPC 기출 중 한개를 풀어봤다. 역시 어려웠다. 그간 안드로이드 스튜디오로
# 앱 프로그래밍 해본다고 백준은 안했는데, 오히려 스트레스만 받았었다.
# 이제 안드로이드 스튜디오는 내려놓기로 했다. 오히려 컴퓨터에 대한
# 흥미만 떨어졌던 것 같다. 좀 더 배우고 난 뒤에 도전해야겠다.

import sys
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


n=int(input())
arr=[]
arrL=[0]*n
num1=0
num2=0
for i in range(n-1):
    tmp=[int(x) for x in sys.stdin.readline().split()]
    tmp[0]-=1
    tmp[1]-=1
    arrL[tmp[0]]+=1
    arrL[tmp[1]]+=1
    arr.append(tmp)
for i in range(n):
    if arrL[i]>=3:
        num2+=ncr(arrL[i],3)
for e in arr:
    num1+=(arrL[e[0]]-1)*(arrL[e[1]]-1)
if num1>num2*3:
    print("D")
elif num1==num2*3:
    print("DUDUDUNGA")
else:
    print("G")
