# 사칙연산, level 4, 푸는 중
# 한 1시간 좀 넘게 해봤는데, 도저희 내 로직이 왜 틀린 것인지 모르겠다
# 일단 보류해 놓고, 나중에 또 풀어봐야겠다.
def solution(arr):
    for i in range(len(arr)):
        if i%2==0:
            arr[i]=int(arr[i])
    ind=1
    ans=arr[0]
    while ind<len(arr):
        if arr[ind]=="+":
            ans+=arr[ind+1]
            ind+=2
        else:
            min_value=arr[ind+1]
            offset=1
            acc=arr[ind+1]
            for i in range(ind+2,len(arr),2):
                if arr[i]=="-":
                    acc-=arr[i+1]
                    if acc<min_value:
                        min_value=acc
                        offset=i+1-ind
                else:
                    acc += arr[i + 1]
            ans-=min_value
            ind+=offset+1
    return ans


print(solution(["5", "-", "5", "-", "5", "+", "25", "+", "5"]))
