# 골드 1, 1시간 가량, 세그먼트 트리 문제.
# 약 1주일 간 시험기간이라 쉬었었다. 이제부턴 방학이기도 하겠다 못해도 매일 1문제는 풀어야 겠다.
# 저번에 구현한 세그먼트 트리에는, 값을 바꾸는 거는 있어도,
# 특정 구간 내의 값을 구하는 것이 없었어서, 그거 새로 만드느라 오래 걸렸다.
# 그리고 tree 짤 때 index 도, 세그먼트 트리 형식으로 짜지 않아서 그것도 수정하느라 좀 걸렸다.
# 이번꺼는 아예 안보고 짠 거라서, 나름 도움이 많이 된 것 같다.
import sys


def initial(a,b,c):
    mid = (b+c)//2
    if b==c:
        tree[a]=arr[b]
    else:
        tree[a]=initial(a*2,b,mid)*initial(a*2+1,mid+1,c)
    return tree[a]


def change(ind, replace_value, cur_in_tree,cur_min,cur_max):
    mid = (cur_min+cur_max)//2
    if cur_min==cur_max:
        tree[cur_in_tree]=replace_value
    elif ind<=mid:
        tree[cur_in_tree]= change(ind, replace_value,cur_in_tree*2,cur_min,mid)*tree[cur_in_tree*2+1]
    else:
        tree[cur_in_tree] = change(ind, replace_value, cur_in_tree * 2+1, mid+1,cur_max) * tree[cur_in_tree * 2]
    return tree[cur_in_tree]


def multiply(multi_min,multi_max,cur_min,cur_max,cur_in_tree):
    global ans
    mid = (cur_min+cur_max)//2
    if multi_min<=cur_min and multi_max>=cur_max:
        ans*=tree[cur_in_tree]
        return
    if multi_min<=mid:
        multiply(multi_min, multi_max, cur_min,mid,cur_in_tree * 2)
    if multi_max>mid:
        multiply(multi_min,multi_max,mid+1,cur_max,cur_in_tree*2+1)
    return


while True:
    try:
        N, T = [int(x) for x in input().split()]
    except (EOFError, ValueError):
        break
    arr = [int(x) for x in sys.stdin.readline().split()]
    tree = [0 for j in range(N*10+1)]
    for i in range(N, N * 2):
        if arr[i-N]>0:
            arr[i-N]=1
        elif arr[i-N]<0:
            arr[i-N]=-1
    initial(1,0,N-1)
    for i in range(T):
        tmp = [x for x in sys.stdin.readline().split()]
        tmp[1]=int(tmp[1])
        tmp[2]=int(tmp[2])
        if tmp[0] == 'P':
            ans = 1
            multiply(tmp[1]-1,tmp[2]-1,0,N-1,1)
            if ans==0:
                ans='0'
            if ans==1:
                ans='+'
            if ans==-1:
                ans='-'
            sys.stdout.write(ans)
        else:
            if tmp[2] > 0:
                tmp[2] = 1
            elif tmp[2] < 0:
                tmp[2] = -1
            change(tmp[1]-1, tmp[2],1,0,N-1)
    print("")
