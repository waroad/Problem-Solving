# 1시간 좀 안되게. 오늘 22년 3월 24일인데, 약 6개월 동안 ps를 안했었다.
# 너무 실력이 떨어진 것 같아서 다시 시작하려 한다. (소마 2차 코테도 떨어졌다..)
# 학부연구실에 들어가서 공부할 시간은 많기에 할일 없으면 종종 하려고 한다.
# 트리 그냥 자식이 없는 애부터 불러스 부모한테 값 넘겨주는 간단한 문제다.
# 지문이 조금 모호한 부분이 있어서 시간이 좀 걸렸다.

from collections import deque


def solution(enroll, referral, seller, amount):
    enroll.insert(0,'---')
    referral.insert(0,'---')
    answer = [0]*len(enroll)
    dict1={}
    par=[0]*len(enroll)
    pro=[[] for _ in range(len(enroll))]
    son=[[] for _ in range(len(enroll))]
    cnt=0
    for i in enroll:
        dict1[i]=cnt
        cnt+=1
    for ind, i in enumerate(referral):
        if ind==0:
            continue
        if i!='-':
            par[ind]=dict1[i]
            son[dict1[i]].append(ind)
        else:
            par[ind]=0
            son[0].append(ind)
    for ind, i in enumerate(seller):
        pro[dict1[i]].append(amount[ind]*100)
    son_len=[len(x) for x in son]
    deq = deque()
    for i in range(len(son)):
        if son_len[i]==0:
            deq.append(i)
    while len(deq):
        tmp=deq.popleft()
        for i in pro[tmp]:
            answer[tmp]+=i-i//10
            if i//10!=0: pro[par[tmp]].append(i//10)
        pro[tmp]=[]
        son_len[par[tmp]]-=1
        if son_len[par[tmp]]==0:
            deq.append(par[tmp])
    answer.pop(0)
    return answer

