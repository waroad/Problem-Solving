# 20분 안팎 큐를 활용하는 문제이다.
# 기존의 큐에서 큐 전체의 최댓값을 구할 수 있는 기능을 O(1) 안에 실행할 수 있게 코드를 짜는 것이 관건이었다.
# 구글링해서 이해하고, 내가 직접 짰다. 큐를 이렇게 2개로 유용하게 쓸 수 있다는 것을 알아서 좋았다.

from collections import deque


def solution(stones, k):
    que1=deque()
    que2=deque()
    for i in range(k):
        que1.append(stones[i])
        if len(que2)==0:
            que2.append([stones[i],i])
        else:
            while len(que2) and que2[-1][0] < stones[i]:
                que2.pop()
            que2.append([stones[i],i])
    answer=que2[0][0]
    for i in range(k,len(stones)):
        que1.append(stones[i])
        while len(que2) and que2[-1][0] < stones[i]:
            que2.pop()
        que2.append([stones[i],i])
        que1.popleft()
        if que2[0][1]==i-k:
            que2.popleft()
        # print(que2)
        if que2[0][0]<answer:
            answer=que2[0][0]
    return answer



print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))