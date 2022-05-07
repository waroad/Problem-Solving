# 5분 컷 했다.
# 슬슬 프로그래머스 3단계 중 최근꺼는 거의 다 풀어서
# (아니면 너무 길어서 귀찮아서 넘긴 문제들만 남았다. 특히 카카오 같은)
# 옛날 3단계 문제들만 남았는데, 얘네들은 확실히 퀄리티도 낮고 난이도도 낮은 것 같다.
def solution(n, s):
    if n>s:
        return [-1]
    arr=[s//n]*n
    for i in range(s%n):
        arr[i]+=1
    arr.reverse()
    return arr


print(solution(2,9))
