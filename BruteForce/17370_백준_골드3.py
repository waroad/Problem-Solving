# 골드 3, 브루트포스, 그래프, 40분 정도
# 이것도 UCPC 문제인데, 처음 문제를 읽었을 때 규칙을 찾아서
# 순열을 푸는 형식으로 문제를 풀려고 했었다. 하지만 규칙을 못찾겠어서
# 조금 구글링을 했더니, 그냥 좌표로 부르트 포스로 풀어야 한다는 것을 봤고,
# 그래서 좌표를 적절히 지정해서 풀었다. 이 문제를 UCPC에서 처음 읽었다면
# 부르트포스 인지 못찾고, DP로 풀어야지 하다가 못풀었을 것 같다. 역시 어렵다.

n= int(input())
arr=[0]*25
cur=[30,30]

cor = [[0 for _ in range(60)] for j in range(60)]
# y가 0일 때는 짝수 x에서 올라가는거, 대각선 밑으로 두개 가능
# y가 1일 때는 짝수 x에서 내려가는거, 대각선 위로 두개 가능
# y가 2일 때는 홀수 x에서 올라가는거, 대각선 밑으로 두개 가능
# y가 3일 때는 홀수 x에서 내려가는거, 대각선 위로 두개 가능


def move(a,b,c,d):
    cor[a][b]=1
    if c>23:
        cor[a][b]=0
        return
    if a%2==0:
        if cor[a+1][b]==0:
            move(a + 1,b,c+1,1)
        elif d!=1:
            arr[c]+=1
        if cor[a-1][b-1]==0:
            move(a - 1,b-1,c+1,2)
        elif d!=3:
            arr[c]+=1
        if cor[a-1][b+1]==0:
            move(a - 1,b+1,c+1,3)
        elif d!=2:
            arr[c]+=1
    if a%2==1:
        if cor[a-1][b]==0:
            move(a - 1,b,c+1,1)
        elif d!=1:
            arr[c]+=1
        if cor[a+1][b-1]==0:
            move(a + 1,b-1,c+1,2)
        elif d!=3:
            arr[c]+=1
        if cor[a+1][b+1]==0:
            move(a + 1,b+1,c+1,3)
        elif d!=2:
            arr[c]+=1
    cor[a][b]=0


move(30,30,1,0)
print(arr[n+1])
