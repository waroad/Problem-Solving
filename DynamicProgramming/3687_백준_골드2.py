# 골드 2, 그리디 & dp 문제, 40분 정도 걸린 것 같다.
# 이것도 골드 2 치고는 쉽다. 확실히 dp, 그리디 문제가 구현하기는 제일 쉬운 것 같다.
# 성냥개비 배치 문제인데 일단 규칙을 찾으려고 한 dp[10]까지 직접해보고, 규칙을 찾아서
# 바로 풀었다.
dp_min=[0]*101
dp_max=[0]*101
dp_min[2]=1
dp_min[3]=7
dp_min[4]=4
dp_min[5]=2
dp_min[6]=6
dp_min[7]=8
dp_max[2]=1
dp_max[3]=7
dp_max[4]=11
dp_max[5]=71


def min1(tmp):  # min1 과 min2 의 내용이 너무 많이 중복돼서 그냥 함수로 만들었다.
    tmp_a=0
    while tmp > 2:
        tmp_a += 8 * pow(10, tmp - 3)
        tmp -= 1
    return tmp_a


def min2(tmp):
    tmp_a=0
    while tmp>1:
        tmp_a+=8*pow(10,tmp-2)
        tmp-=1
    return tmp_a


def find_min():
    t=8
    while t<101:
        tmp=(t-1)//7+1
        tmp1=t%7
        tmp2=0
        if tmp1==1:
            tmp2=10*pow(10,tmp-2)
            tmp2+=min1(tmp)
        if tmp1==2:
            tmp2=1*pow(10,tmp-1)
            tmp2+=min2(tmp)
        if tmp1==3:
            tmp2 = 200 * pow(10, tmp - 3)
            tmp2+=min1(tmp)-8*pow(10,tmp-3)
        if tmp1==4:
            tmp2 = 20 * pow(10, tmp - 2)
            tmp2+=min1(tmp)
        if tmp1==5:
            tmp2 = 2 * pow(10, tmp - 1)
            tmp2+=min2(tmp)
        if tmp1==6:
            tmp2 = 6 * pow(10, tmp - 1)
            tmp2+=min2(tmp)
        if tmp1==0:
            tmp2 = 8 * pow(10, tmp - 1)
            tmp2+=min2(tmp)
        dp_min[t]=tmp2
        t+=1


def find_max():
    t = 3
    while t < 101:
        dp_max[t]=0
        tmp=t//2
        if t%2==0:
            dp_max[t]+= pow(10, tmp-1)
        else:
            dp_max[t] += 7 * pow(10, tmp - 1)
        while tmp > 1:
            dp_max[t] += pow(10, tmp - 2)
            tmp -= 1
        t+=1


find_min()
find_max()
dp_min[10]=22
N=int(input())
for i in range(N):
    tmp_t=int(input())
    print(dp_min[tmp_t],dp_max[tmp_t])
