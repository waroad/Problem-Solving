# 플레 2, 분할 정복 2시간 하고 못풀고 풀이 봄
# 이게 학교 과제로 나와서 플레 2라 조금 높은 감은 있었는데, 역시는 역시다.
# 설명 없이 하려니 어렵네..
# 근데 학교 과제는 여기서 시간을 한번 더 단축하는 것이어서, 최소 플레 2의
# 난이도다. 일단은 풀어보려고 한다.
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