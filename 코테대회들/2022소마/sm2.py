n,m,k=[int(x) for x in input().split()]
arrN=[0]*(n+1) # 만족도 조사 기록한 사람들
arrN_N=[[0,0] for _ in range(n+1)]  # root 인 한 친구에 대해서 [만족도 조사 친구 관계 중 한 사람 수, 전체 평균]
for i in range(m):
    tmp=[int(x) for x in input().split()]
    arrN[tmp[0]]=tmp[1]

level=[0]*(n+1)
root_id=[i for i in range(n+1)]
node_pr=[i for i in range(n+1)]


def find_pr(a):
    if node_pr[a]!=a:
        return find_pr(node_pr[a])
    else:
        return a


for i in range(k):
    tmp=[int(x) for x in input().split()]
    if root_id[tmp[0]]==root_id[tmp[1]]:
        continue
    else:
        a_pr=find_pr(tmp[0])
        b_pr=find_pr(tmp[1])
        if level[a_pr]>level[b_pr]:
            node_pr[b_pr]=a_pr
            level[a_pr]+=1
            root_id[tmp[1]]=a_pr
        else:
            node_pr[a_pr]=b_pr
            level[b_pr]+=1
            root_id[tmp[0]]=b_pr

for i in range(1,n+1):
    if arrN[i]!=0:
        arrN_N[root_id[i]][0]+=1
        arrN_N[root_id[i]][1]+=arrN[i]
minus_cnt=0 # 만족도 조사 전체 평균에서 뺄 사람들
for i in range(1,n+1):
    if arrN[i]==0:
        if arrN_N[root_id[i]][0]==0:
            minus_cnt+=1
            continue
        arrN[i]=arrN_N[root_id[i]][1]//arrN_N[root_id[i]][0]

print(format(sum(arrN)/(n-minus_cnt),'.2f'))