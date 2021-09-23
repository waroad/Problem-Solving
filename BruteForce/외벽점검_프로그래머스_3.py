# 3단계, BruteForce, 순열, 1시간 가량
# 구현이랑 BruteForce, DFS BFS 이쪽 부분은 거의 마스터 했다고 느꼈는데(물론 골드 수준)
# 이건 조금 어려웠다. 동그란 모양을 배열에 담았을 때 처음과 끝을 어떻게 연결할까 종종 고민했는데, 
# 배열을 두배로 곱해준 다음 계산하면 된다는 것을 알았다.
# 그 다음에는 그냥 다 대입해보면 된다.

import itertools


def solution(n, weak, dist):
    global ans
    L=len(weak)
    for i in range(len(weak)):
        weak.append(n+weak[i])
    ans=10000

    def check(li):
        arr=li[:]
        global ans
        for i in range(L):
            cur=i
            init=i
            li=arr[:]
            for j in range(len(li)):
                while cur<L*2-1 and li[j]>=weak[cur+1]-weak[cur]:
                    li[j]-=weak[cur+1]-weak[cur]
                    cur+=1
                cur+=1
                if cur-init>=L:
                    if j<ans:
                        ans=j
                    break

    result = list(itertools.permutations(dist,len(dist)))
    for i in result:
        check(list(i))
    if ans==10000:
        ans=-2
    return ans+1



