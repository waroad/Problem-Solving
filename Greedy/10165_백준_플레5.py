# 플레 5, 그리디, 원형, 스위핑, 30분 정도.
# 오늘 또 풀면서 느낀게 그리디는 진짜 문제 해결 능력을
# 요구하는 것 같다. 큰 스킬도 필요 없고, 복잡한 알고리즘도 없으면
# 진짜 어떻게 정렬하고 어떻게 for 구문 돌리는지 말이다.
# 개인적으로 백준 플레 문제 1개를 풀어야 한다고 하면, 모든 그리디가 쉽지는
# 않겠지만 그래도 그리디가 가장 맞출 확률이 높을 것 같다.
# 이 문제는 원형의 순환 1차선에 여러개의 선분이 그어져있고, 하나의 선분에
# 완전히 속하는 다른 선분이 있으면, 그런 선분들을 제외한 나머지 선분들을 구하는
# 문제이다. 백준에서 그리디 문제 중 제일 처음 나오는 플레 5 문제라서 몇번
# 옛날에 읽어본 적은 있었는데, 이번에 맞추게 되어서 좋다. 확실히 내가 성장하긴 한 것 같다.
# 스위핑은 다 풀고 나서 저런 알고리즘이 사용되었다는 것을 알았는데, 별로 스킬이 있는
# 알고리즘은 아니고 그냥 생각해낼 수 있는 정도다.

from operator import itemgetter
import sys
n=int(input())
m=int(input())
arr=[]  # 맨 처음 모든 선분을 담을 배열. 출발점이 작은 순으로 정렬한다.
arr2=[]  # 만약 출발점이 같은 선분들이 있다면, 그 중 도착점이 제일 뒤인 선분들만 남겨 놓는 배열
arr3=[]  # arr2 에서 이제 겹쳐지지 않는 선분들만 추출해서 넣어준다. 원래는 이게 바로 정답이겠지만, 원형이기에 한번 더 해줘야 한다.
ans=[]  # arr3 에서, 원형의 특성을 고려해 맨 앞의 선분들을 다시 한번 비교해준다.
for i in range(m):
    tmp=[int(x) for x in sys.stdin.readline().split()]
    tmp.append(i+1)
    if tmp[0]>tmp[1]:
        tmp[1]+=n
    arr.append(tmp)
arr.sort(key=itemgetter(1),reverse=True)
arr.sort(key=itemgetter(0))
cur=-1
for i in arr:
    if i[0]>cur:
        cur=i[0]
        arr2.append(i)
maxV=0
res=-1
for i in arr2:
    if i[1]>maxV:
        maxV=i[1]
        arr3.append(i)
        if i[1]>=n:
            res=i[1]
res-=n
for i in arr3:
    if i[1]>res:
        ans.append(i[2])
ans.sort()
print(*ans)
