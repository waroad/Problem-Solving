# 그리디, 수학, 골드2, 1시간
# UCPC 기출 문제로 이거는 알고리즘 보다는 수학 문제였다.
# 임의의 좌표를 하나 정해서 주어진 모든 좌표와의 거리값 중 최소를 갖는 값과
# 최대를 갖는 값의 평균을 구하는 문제인데 30분 좀 넘게 고민해 보고 답이 잘 안나와서 구글링 좀 해보았더니
# 그냥 주어진 좌표 중 하나를 최솟값으로 설정해도 답이 된다고 하였다. 그것을 알고나서는 바로 풀었다.
# 이런 수학 문제도 좀 까다로운 것 같다.

n=int(input())
arr=[]
for i in range(n):
    tmp=[int(x) for x in input().split()]
    arr.append(tmp)
distance=100000000
coordinate=0
for i in range(n):
    tmp_dis=0
    for j in range(n):
        if i==j: continue
        tmp=(arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2
        if tmp>tmp_dis: tmp_dis=tmp
    if tmp_dis<distance:
        distance=tmp_dis
        coordinate = i
print(*arr[coordinate])
