# 레벨 3, 세그먼트 트리, 40분 정도
# 구간 최댓값이 필요하다고 판단해서 세그먼트 트리로 풀었다.
# 인풋이 만 개 밖에 안돼서 세그먼트 트리로 딱히 풀지 않아도 되는 문제이긴 한데, 오랜만에 세그먼트 트리 개념도 다시 한 번
# 익힐겸 풀어봤다. 옛날에 풀었던 코드를 봤는데, 그 때는 a//b 도 몰라서 int()로 감싸줬었다. 그 때 보다는 조금 문법이 매끄러워 졌을지도.
# 딱히 어려운 건 없었다.

def solution(nodeinfo):
    for ind,node in enumerate(nodeinfo):
        node.append(ind+1)
    nodeinfo.sort()
    arr=[0]*len(nodeinfo)*4
    answer=[[],[]]
    
    def MM(a, b, ind):  # 세그먼트 트리 구간 별 최대 값 구하기
        if a == b:
            arr[ind] = [nodeinfo[a][1],nodeinfo[a][2],a]
            return arr[ind]
        else:
            tm1 = MM(a, (a + b) // 2, ind * 2)
            tm2 = MM((a + b) // 2 + 1, b, ind * 2 + 1)
            arr[ind] = tm2
            if tm1[0] > tm2[0]:
                arr[ind] = tm1
            return arr[ind]
    
    def preorder(l, r, a, b, c):
        ans1=interval_max(l, r, a, b, c)
        answer[0].append(ans1[1])
        if l<=ans1[2]-1:
            preorder(l, ans1[2]-1, a, b, c)
        if r>=ans1[2]+1:
            preorder(ans1[2]+1,r, a, b, c)

    def postorder(l, r, a, b, c):
        ans1=interval_max(l, r, a, b, c)
        if l<=ans1[2]-1:
            postorder(l, ans1[2]-1, a, b, c)
        if r>=ans1[2]+1:
            postorder(ans1[2]+1,r, a, b, c)
        answer[1].append(ans1[1])

    # l,r 은 구하려는 범위의 좌우, a,b 는 현재 탐색하고 있는 범위, c는 현재 탐색하고 있는 범위의 세그먼트 트리 좌표입니다.
    def interval_max(l, r, a, b, c):
        c1 = 0
        c2 = 0
        m=(a + b) // 2
        if l == a and r == b:
            return arr[c]
        if l <= m:
            c1 = 1
            if r <= m:
                t1 = interval_max(l, r, a, m, c * 2)
            else:
                t1 = interval_max(l, m, a, m, c * 2)
        if r > m:
            c2 = 1
            if l > m:
                t2 = interval_max(l, r, m + 1, b, c * 2 + 1)
            else:
                t2 = interval_max(m + 1, r, m + 1, b, c * 2 + 1)
        if c1 and c2:
            if t1[0]>t2[0]:
                return t1
            return t2
        if c1:
            return t1
        if c2:
            return t2
    MM(0, len(nodeinfo)-1, 1)
    preorder(0,len(nodeinfo)-1,0,len(nodeinfo)-1,1)
    postorder(0,len(nodeinfo)-1,0,len(nodeinfo)-1,1)
    return answer

