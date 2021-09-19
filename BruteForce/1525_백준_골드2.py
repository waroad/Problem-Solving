# 골드 2, BFS, 큐, 1시간 30분
# 덱큐 안에다가 가능한 모든 경우의 수를 넣어서 3x3 퍼즐을 푸는 문제이다.
# 메모리를 32mb로 제한해 놓아서, 풀기 위해 최소한의 메모리만 썼어야 했다.
# 기존에 list와 달리 dict가 어떤 값이 있는지 없는지 찾기 위해서는
# 정말 빠르고 좋다는 것을 알게 해준 문제이다.

from collections import deque

dict1={}
arr=[[x for x in input().split()] for _ in range(3)]
tmp_str=''
for i in range(3):
    for j in range(3):
        tmp_str+=str(arr[i][j])
queue = deque([[tmp_str,0]])
arr1 = [[0] * 3 for _ in range(3)]
kk=0
while queue:
    tmp,num=queue.popleft()
    cnt=0
    if tmp=='123456780':
        kk=1
        print(num)
        break
    for i in range(3):
        for j in range(3):
            arr1[i][j]=int(tmp[cnt])
            cnt+=1
    for i in range(3):
        for j in range(3):
            if arr1[i][j]==0:
                if i>0:
                    arr1[i-1][j]+=10
                if i<2:
                    arr1[i+1][j]+=10
                if j>0:
                    arr1[i][j-1]+=10
                if j<2:
                    arr1[i][j+1]+=10
    for i in range(3):
        for j in range(3):
            if arr1[i][j]>10:
                tmp1=tmp
                tmp1=tmp1.replace('0',tmp1[i*3+j])
                tmp1 = tmp1[:i*3+j] + '0' + tmp1[i*3+j + 1:]
                if tmp1 in dict1:
                    continue
                dict1[tmp1] = 1
                queue.append([tmp1,num+1])

if len(queue)==0 and kk==0:
    print("-1")
