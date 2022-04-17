# 2시간 정도 걸렸다. 시험기간인데 이게 뭔 고생인지;
# 일단 처음 컨셉을 이해하는데도 시간이 30분 정도 걸렸다.
# 이게 금과 은을 동시에 담을 수 있는 트럭이 여러 대 있을 때,
# 어떻게 효율적으로 금, 은을 배분해서 담으면 최소 시간안에 다 옮길 수 있을까인데,
# 구하는 방법은 금을 최대로 담은 경우와 은을 최대로 담은 경우가 각각 목표량보다 높고,
# 금 최대의 금+은 의 값이 목표한 금+은의 값보다 크면 된다.
# 그래서 이거를 priority queue 로 짰는데 priority queue 가 느려서 heapq 로 갈아타서
# 짰었다. 근데 이게 참 악질인게 1개의 경우 빼고는 다 통과 한다. 1개의 경우만 시간초과인데,
# 그래서 좀만 하면 되겠거니 했는데 암만 해도 안됐고, 그래서 결국은 눈물을 머금고 이분탐색으로
# 갈아탔다. 근데 이분탐색도 참 악질인게 무슨 40 조 인가 까지 가야된다. 이분탐색에서 초반
# 6개가 틀리길래 예외처리를 잘못 했나 하고 봤더니 최댓값을 높이니까 해결됐고,
# 이 최댓값을 높이니까 다른 애들이 시간초과가 나서, 아래와 같이 초기 최댓값은 낮게 해놓고,
# h 가 l 과 같아지면 h 를 높이는 방식으로 했다. 그래도 조금 배우긴 했다.
# 역시 이분탐색은 구현하기도 싫고 짜증난다.

def solution(a, b, g, s, w, t):
    length=len(g)
    l=0
    h=40000000002
    while l<h:
        g_best=[0]*2
        s_b=0
        g_best1=[0]*2
        s_b1=0
        m=(h+l)//2
        for i in range(length):
            if m<t[i]:
                continue
            g_best[0]+=min(((m-t[i])//(t[i]*2))*w[i] + w[i],g[i])
            if ((m-t[i])//(t[i]*2))*w[i] + w[i]>g[i]:
                g_best[1]+=min(((m-t[i])//(t[i]*2))*w[i] + w[i]- g[i],s[i])
            s_b+=min(((m-t[i])//(t[i]*2))*w[i] + w[i],s[i])
        for i in range(length):
            if m-1<t[i]:
                continue
            g_best1[0]+=min(((m-1-t[i])//(t[i]*2))*w[i] + w[i],g[i])
            if ((m-1-t[i])//(t[i]*2))*w[i] + w[i]>g[i]:
                g_best1[1]+=min(((m-t[i]-1)//(t[i]*2))*w[i] + w[i]- g[i],s[i])
            s_b1+=min(((m-1-t[i])//(t[i]*2))*w[i] + w[i],s[i])

        if g_best[0]>=a and s_b>=b and sum(g_best)>=a+b and \
            (g_best1[0]<a or s_b1<b or sum(g_best1)<a+b):
            return m
        elif g_best[0]<a or s_b<b or sum(g_best)<a+b:
            l=m+1
        else:
            h=m
        if l==h:
            h=h*100000
