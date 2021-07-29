# 골드 3, 그리디, 10분도 안걸림
# 문제가 주어진 추들로 만들 수 없는 최소 자연수 값을 구하는 것인데,
# 이와 비슷한 개념을 초등학교 때 수학시간에 한 적이 있어서 쉽게 구했다.
# 확실히 그리디가 난이도가 체감상 훨씬 쉬운 것 같다.

n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
sum1=0
for i in range(n):
    if arr[i]>sum1+1:
        break
    else:
        sum1+=arr[i]

print(sum1+1)
