# 그리디, 플레 5, 약 30분 축구 토너먼트 결과가 성립하는지 확인하는 문제
# 짧게 걸리긴 했지만 무척 도박성이 강한 문제였다.
# 정확히 이렇게 하면 풀리겠지 하고 푼 것이 아니라, 그리디의 특성 상
# 이런 식으로 짜던데, 한 번 이렇게 짜볼까 하고 푼게 정답이었다.
# 지금 식은 제일 승수 적은 팀부터 없애주는 건데, 이것의 반례가 없다고
# 장담 못하는 상황에서 그냥 냈는데 맞았다. 오늘부로 플레5를 찍었다.

N= int(input())
arr=[int(x) for x in input().split()]
arr.sort(reverse=True)
for i in range(N-1,0,-1):
    #print(arr)
    if len(arr)-arr[i]-1>len(arr):
        break
    for j in range(0,len(arr)-arr[i]-1):
            arr[j]-=1
    arr.pop()
    arr.sort(reverse=True)

if arr[0]!=0: print(-1)
else: print(1)
