# 플레 2, 분할 정복 2시간 하고 못풀고 풀이 봄
# 이게 학교 과제로 나와서 플레 2라 조금 높은 감은 있었는데, 역시는 역시다.
# 설명 없이 하려니 어렵네..
# 근데 학교 과제는 여기서 시간을 한번 더 단축하는 것이어서, 최소 플레 2의
# 난이도다. 일단은 풀어보려고 한다.
# 결국 그냥 이것도 나중에 답을 보고 이해하는 식으로 했다.
# 파이썬은 set 의 lower bound 를 지원을 안해서, difultdict 라는 모듈로
# dict 안에 deque 를 넣고, 2차원 계산을 할 때 허수 진수로 하면
# 거리를 계산하기 편하다는 것을 이용해 풀었다. 그냥 풀라 하면 절대 못푸는
# 난이도였다.
# 여기 삽질한 10시간 가까이가 참.. 너무하긴 하다.
# 건진 것이 있다면 bisect 라는 모듈이 lower bound, upper bound 를 쉽게 구해준다.
# 이분 탐색에서 어디 넣을지 계산해야 하는 문제에서, 한줄로 바로 해결해주는 모듈인 것이다.
import sys
n=int(input())
arr=[[int(x)+10000 for x in sys.stdin.readline().split()] for _ in range(n)]
arr.sort(key = lambda x: x[0])


def find(a,b):
    if a==b:
        return 1000000000
    elif a+1==b:
        return (arr[a][0]-arr[b][0])**2 + (arr[a][1]-arr[b][1])**2

    m=(a+b)//2
    tmp=min(find(a,m), find(m+1,b))
    comp_arr=[]
    for i in range(m+1,b+1):
        if (arr[m][0]-arr[i][0])**2<tmp:
            comp_arr.append(arr[i])
        else:
            break
    for i in range(m, a-1, -1):
        if (arr[m][0]-arr[i][0])**2<tmp:
            comp_arr.append(arr[i])
        else:
            break
    comp_arr.sort(key = lambda x: x[1])
    for i in range(len(comp_arr)-1):
        for j in range(i+1,len(comp_arr)):
            if (comp_arr[i][1] - comp_arr[j][1]) ** 2 > tmp:
                break
            else:
                tmp = min(tmp, (comp_arr[i][1] - comp_arr[j][1]) ** 2
                          + (comp_arr[i][0] - comp_arr[j][0]) ** 2)
    return tmp


find(0,len(arr)-1)
print(find(0,len(arr)-1))