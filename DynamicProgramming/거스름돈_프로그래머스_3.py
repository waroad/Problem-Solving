# 시험이 어제 다 끝나서 이제 다시 하루 한문제씩 하려한다.
# 이거는 3단계 dp 인데 탑다운으로 하면 효율성에서 아쉽게 2개만 시간초과다..
# 바텀 투 탑으로 다시 짜고 있는데 시간이 없어서 내일 다시 해야겠다.
# + 그냥 탑다운으로도 시간을 줄여서 겨우겨우 통과했다.
# 이걸로 1시간 반은 쏟았는데.. 생각보다 어렵네
# 일반적인 거스름돈 문제다. 파이썬이 아니었으면 훨씬빨리 통과했을텐데.
def solution(n, money):
    dict1={}

    def find(a,used):
        b=str(a)+'x'+str(used[-1])
        if b in dict1:
            return dict1[b]
        tmp=0
        if len(used)==2:
            for i in range(a,-1,-used[1]):
                if i%used[0]==0:
                    tmp+=1
        else:
            used_v = used.pop()
            for i in range(a,-1,-used_v):
                tmp+=find(i,used)
            used.append(used_v)
        dict1[b]=tmp
        return tmp
    ans=find(n,money)
    return ans

