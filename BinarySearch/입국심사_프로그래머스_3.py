# 1시간 정도 걸렸다. 3단계인데 생각보다 오래 걸렸다.
# 바이너리 서치를 하는 기본적인 문제인데, 이게 INPUT 값이 10억까지이고, 정답은 1000억도 훌쩍 넘을 수도 있어서
# 그걸 고려 못하느라 조금 걸렸다. 그래서 binary search max 값인 h 를 저렇게 엄청 높게 설정했더니
# 통과했다. 그거 외에도, 이걸 binary search 문제라는 것을 인지하는데도 30분 가까이 걸린
# 생각보다 많이 헤멘 문제였다. binary search 오랫만에 직접 해봐서 좋았다. high, low
# 이용 안하고 delta 값을 계속 2로 나누어 주며 했었는데, 이걸 다시 high, low 로 해야한다는 것도
# 까먹고 있었다.

def solution(n, times):
    times.sort()
    h=1000000000000000
    l=0
    tmp=0
    while True:
        k=(h+l)//2
        tmp2=0
        for i in times:
            tmp+=k//i
            tmp2+=(k-1)//i
        if tmp>=n>tmp2:
            break
        elif tmp>n:
            h=k
        elif tmp<n:
            l=k+1
        else:
            h=k
        tmp=0
    return k


solution(292229226,[700])