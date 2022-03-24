# 정확히 어떤 알고리즘인지는 모르겠다. 아마도 위상정렬인 것 같다.
# 트리가 있을 때, 리프 노드부터 배열에 넣는데, 이 때 리프 트리 index 의 값이
# 낮은 순서로 넣고, 해당 리프는 잘라서 버린다. 그러면 바로 위에 또 하나의 리프
# 리프가 생기고, 또 이 리프들을 비교하며 넣는 거다.
# 시간초과가 떠서, 어짜피 낮은 index 부터 지우기에 각 노드 별 자식들을 sort 한 번
# 해주니 바로 통과했다. 근데 이것을 생각해내기까지 꽤 시간이 걸려 이것도 약 1시간
# 정도 걸렸다.

from heapq import heappush, heappop


def solution(ranges):
    max1=0
    que=[]
    answer=[]
    tmp=0
    for x in ranges:
        max1=max(x[0],max1)
        max1=max(x[1],max1)
    n=[[] for _ in range(max1+1)]
    cnt=[0]*(max1+1)
    for x in ranges:
        n[x[0]].append(x[1])
        n[x[1]].append(x[0])
        cnt[x[0]]+=1
        cnt[x[1]]+=1
    for i in range(len(n)):
        n[i].sort()
        if cnt[i]==1:
            heappush(que,[i,n[i][0]])
            cnt[i]-=1
            n[i].pop()
    while que:
        tmp=heappop(que)
        answer.append(tmp[0])
        cnt[tmp[1]]-=1
        if len(n[tmp[1]]):
            n[tmp[1]].remove(tmp[0])
            if cnt[tmp[1]]==1:
                heappush(que, [tmp[1], n[tmp[1]][0]])
                cnt[tmp[1]] -= 1
                n[tmp[1]].pop()
    return answer


print(solution([[2,1],[1,3]]))
