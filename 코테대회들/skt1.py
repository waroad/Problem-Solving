def solution(p):

    answer = [0]*len(p)
    for i in range(len(p)):
        min_val=10000000
        min_ind=len(p)-1
        for j in range(i,len(p)):
            if p[j]<min_val:
                min_val=p[j]
                min_ind=j
        if min_ind!=i:
            answer[min_ind]+=1
            answer[i]+=1
            tmp=p[i]
            p[i]=p[min_ind]
            p[min_ind]=tmp
        print(p)
        print("-",answer)
    return answer

print(solution([2,5,3,1,6]))