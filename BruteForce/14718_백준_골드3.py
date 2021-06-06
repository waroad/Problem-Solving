# 골드 3, 값 좌표 압축, 브루트포스, 1시간 좀 안되게.
# 원래 세그먼트 트리 문제를 하나 풀려다가, 거기서 좌표 압축 기법이 쓰인다길래
# 아직 좌표 압축 기법을 써본적이 없어 한 번 풀어봤다.
# 이 문제는 근데 좌표 압축 보다는 그냥 부르트 포스 어떻게 짤지 고민하다가 조금 오래 걸렸다.

n, K = [int(x) for x in input().split()]

arr1=[[0,_] for _ in range(n)]
arr2=[[0,_] for _ in range(n)]
arr3=[[0,_] for _ in range(n)]
for _ in range(n):
    arr1[_][0],arr2[_][0],arr3[_][0] = [int(x) for x in input().split()]
arr1.sort()
arr2.sort()
arr3.sort()
arr_cnt = [0] * n
ans=10000000000
tmp_cnt=0
for i in range(n):
    arr_cnt[arr1[i][1]] += 1
    if arr_cnt[arr1[i][1]] == 3:
        tmp_cnt += 1
    for j in range(n):
        arr_cnt[arr2[j][1]] += 1
        if arr_cnt[arr2[j][1]] == 3:
            tmp_cnt += 1
        for k in range(n):
            arr_cnt[arr3[k][1]] += 1
            if arr_cnt[arr3[k][1]] == 3:
                tmp_cnt += 1
            if tmp_cnt==K:
                if arr1[i][0]+arr2[j][0]+arr3[k][0]<ans:
                    ans = arr1[i][0]+arr2[j][0]+arr3[k][0]
        for k in range(n):
            arr_cnt[k]-=1
            tmp_cnt=0
    for j in range(n):
        arr_cnt[j] -= 1
        tmp_cnt=0
print(ans)
