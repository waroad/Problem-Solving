# 지금까지 풀어본 레벨 3 중에는 거의 제일 쉬운 것 같다.
# 5분 정도 걸린 것 같다. 팰린드롬 구하는 건데 S의 범위가 2500까지밖에 안된다 해서
# 그냥 2중 루프로 다 계산했다. 시험기간이기도 하고 하니까 쉬어가는 느낌으로 풀었다.
def solution(s):
    ans = 1

    for i in range(len(s)):
        tmp = i
        tt = 1
        while True:
            if tmp >= tt and tmp + tt < len(s) and s[tmp - tt] == s[tmp + tt]:
                tt += 1
            else:
                break
        ans = max(ans, (tt - 1) * 2 + 1)
        tmp = i
        tt = 1
        while True:
            if tmp + 1 >= tt and tmp + tt < len(s) and s[tmp - tt+1] == s[tmp + tt]:
                tt += 1
            else:
                break
        ans = max(ans, (tt - 1) * 2)
    return ans
