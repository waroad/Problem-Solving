# 다음 날 내가 짰던 코드가 뭐가 문제였는지 곰곰히 생각해봤다.
# 그 결과, 내가 짰던 코드는, 기댓값을 구할 때 바로 다음 주사위만 고려해서 구한다는 것이 문제였다.
# 그렇기에 내가 짰던 코드는, 3번 주사위를 굴린 상태부터 시작했는데, 이 방법이 아니라 굴릴 수 있는
# 마지막 주사위부터 거꾸로 가며 dp를 했어야 했다. 그래서 이를 숙지하고 내가 짰던 코드를 수정해 짤 수 있었다.
# 이 방법은 구글에도 없는 방법이다! 구글에는 다 4차원 배열을 쓰지만 3차원 배열만 썼다!
# 기분이 좋다.

N=int(input())
dp2 =[[[0 for _ in range(6)] for _ in range(6)] for _ in range(N-1)]
ans=0


def prize(i,j,k):
    if i == j == k:
        return 10000 + (k + 1) * 1000
    elif i == j:
        return 1000 + (j + 1) * 100
    elif i == k:
        return 1000 + (k + 1) * 100
    elif j == k:
        return 1000 + (k + 1) * 100
    else:
        return (max([i, j, k]) + 1) * 100


for n in range(N-2):
    for i in range(6):
        for j in range(6):
            for k in range(6):
                cur_val=prize(i,j,k)
                expected_val=dp2[n][j][k]
                expected_val=expected_val/6
                if expected_val<cur_val or n==N-2:
                    dp2[n+1][i][j] += prize(j,i,k)
                else:
                    dp2[n+1][i][j]+=expected_val

for i in range(6):
    for j in range(6):
        ans+=dp2[N-2][i][j]
print(ans/216)
