# 사칙연산, level 4, 푸는 중
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


print(solution(["999","-","1000","+","999","-","1000","-","1000","+","999","+","999","-","1000","+","999"]))