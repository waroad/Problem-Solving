from operator import itemgetter

ans = 1000000


def solution(alp, cop, problems):
    global ans
    algo_need=0
    code_need=0

    problems1 = [problems[i] for i in range(len(problems))]
    for i in problems1:
        algo_need=max(algo_need,i[0])
        code_need=max(code_need,i[1])
    problems1.append([0,0,1,0,1])
    problems1.append([0,0,0,1,1])
    problems1.sort(key=itemgetter(1))
    problems1.sort(key=itemgetter(0))
    pp={}

    def dfs(a,b,c):
        global ans
        if str(a)+str(b)+str(c) in pp:
            return
        pp[str(a)+str(b)+str(c)]=1
        if a>=algo_need and b>=code_need:
            ans=min(ans,c)
            return
        for i in problems1:
            if i[0]<=a and i[1]<=b:
                if b>=code_need:
                    if i[2]>0:
                        dfs(a+i[2],b+i[3],c+i[4])
                elif a>=algo_need:
                    if i[3]>0:
                        dfs(a+i[2],b+i[3],c+i[4])
                else:
                    dfs(a+i[2],b+i[3],c+i[4])

    dfs(0,0,0)
    print(ans)
    return ans


solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])
