from bisect import bisect_left


def solution(n, plans, clients):
    answer = []
    arr1=[-1]*(n+1)  # index 의 부가서비스가 최초로 나오는 요금제 index
    plans1=[]
    for ind,i in enumerate(plans):
        tmp=i.split()
        extra_service=[int(x) for x in tmp[1:]]
        extra_service.sort()
        for j in extra_service:
            arr1[j]=ind
        plans1.append(int(tmp[0]))
    for i in clients:
        tmp = i.split()
        extra_service=[int(x) for x in tmp[1:]]
        start_ind=-1
        do_next=0
        for j in extra_service:
            if arr1[j]==-1:
                answer.append(0)
                do_next=1
                break
            if arr1[j]>start_ind:
                start_ind=arr1[j]
        if do_next:
            continue
        if int(tmp[0])>plans1[-1]:
            answer.append(0)
            continue
        min_data=bisect_left(plans1,int(tmp[0]))
        start_ind=max(start_ind,min_data)
        answer.append(start_ind+1)
    return answer


print(solution(5, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"]))