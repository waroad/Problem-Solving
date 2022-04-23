# 시험이 어제 다 끝나서 이제 다시 하루 한문제씩 하려한다.
# 이거는 3단계 dp 인데 탑다운으로 하면 효율성에서 아쉽게 2개만 시간초과다..
# 바텀 투 탑으로 다시 짜고 있는데 시간이 없어서 내일 다시 해야겠다.
def solution(n, money):
    dict1={}

    def find(a,used):
        if str(a)+'x'+str(used) in dict1:
            return dict1[str(a)+'x'+str(used)]
        tmp=0
        used_v=used.pop()
        if len(used)==1:
            for i in range(a // used_v + 1):
                if (a-i*used_v)%used[0]==0:
                    tmp+=1
        else:
            for i in range(a//used_v+1):
                tmp+=find(a-i*used_v,used)
        used.append(used_v)
        dict1[str(a)+'x'+str(used)]=tmp
        return tmp
    # money.sort()
    ans=find(n,money)
    print(dict1)
    # tt=[]
    # dict2={}
    # for i in range(len(money)):
    #     tt.append(money[i])
    #     tmp=0
    #     for j in range(n//tt[-1]+1):
    #         tmp+=dict2[str(n-j*money[-1])]
    #     dict2[str(n)]=tmp
    return ans


print(solution(15, [1, 2,3,4, 5]))
print(solution(10, [1, 2,3, 5]))
print(solution(5, [1, 2, 5]))
