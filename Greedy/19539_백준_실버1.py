# 실버1, 15분, 그리디 알고리즘
# UCPC는 동 난이도 대비 어려운 것 같아서 문제 푸는게 스트레스라 오랫만에 쉬운거 풀어봤다.
# 실버1도 쉽지 않았다. 그래도 뭐. 확실히 쉽긴 하다.

n=int(input())
arr=[int(x) for x in input().split()]
arr.sort(reverse=True)

S=sum(arr)
S2=0
if S%3:
    print("NO")
else:
    for i in range(len(arr)):
        S2+=arr[i]//2
    if S2>=S//3:
        print("YES")
    else:
        print("NO")
