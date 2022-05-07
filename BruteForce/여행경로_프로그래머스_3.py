# dfs 문제, 오랫만에 풀어서 약간 감을 잘못잡아 30분 정도 걸렸다.
# while 로만 풀려고 했는데 역시 안돼서 재귀로 했다.
# defaultdict 를 앞으료 애용할 것 같다.
from collections import defaultdict


def solution(tickets):
    def find(value):
        if len(answer)>len(tickets):
            return 1
        if len(dict2[value]):
            for ind, i in enumerate(dict2[value]):
                if i == 'used': continue
                tmp = i
                dict2[value][ind]='used'
                answer.append(tmp)
                if find(tmp):
                    return 1
                dict2[value][ind]=tmp
                answer.pop()
    dict2 = defaultdict(list)
    for i in tickets:
        dict2[i[0]].append(i[1])
    for i in dict2:
        dict2[i].sort()
    answer = ["ICN"]
    find("ICN")
    return answer
