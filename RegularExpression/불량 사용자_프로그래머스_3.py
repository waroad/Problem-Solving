# 정규식, 약간의 dfs 문제, 30분정도. 정규식 오랫만에 해서 구글링 해보고 하느라 조금 걸렸다.
# 그냥 정규식 문제이다. 카카오 2019 인턴쉽 문제인데, 왠지 풀어본 것 같은 느낌
# 카카오 문제는 다 비슷한가 보다.
import re
ans=0


def solution(user_id, banned_id):
    global ans
    ban=[]
    for b in banned_id:
        b = ['.' if x == '*' else x for x in b]
        b.insert(0,'^')
        b.append('$')
        ban.append(''.join(b))
    # print(ban)
    pos=[[] for _ in range(len(ban))]
    for ind, k in enumerate(ban):
        p=re.compile(k)
        for ind2, i in enumerate(user_id):
            if p.match(i):
                pos[ind].append(ind2)
    pos = sorted(pos, key=len)
    # print(pos)
    ans_t=[]
    dict1={}
    print(pos)

    def tt(a):
        global ans
        if a == len(pos):
            tt2=sorted(ans_t)
            if str(tt2) not in dict1:
                dict1[str(tt2)]=0
                ans+=1
            return
        for j in pos[a]:
            if j not in ans_t:
                ans_t.append(j)
                tt(a+1)
                ans_t.pop()
    tt(0)
    # print(dict1)
    return ans
