def solution(queue1, queue2):

    que=queue1+queue2
    t1=len(queue1)-1
    que_sum=[0]*len(que)
    que_sum[0]=que[0]
    for i in range(1,len(que)):
        que_sum[i]+=que_sum[i-1]+que[i]
    value=que_sum[-1]//2
    ans=[]
    f=0
    r=0
    while que_sum[r]<value:
        r+=1
    qq=len(que)
    if que_sum[r]==value and r>=t1:
        return r-t1
    while r<qq:
        if que_sum[r]-que_sum[f]==value:
            if r>=t1:
                ans.append([f,r])
            r+=1
        elif que_sum[r]-que_sum[f]>value:
            f+=1
        else:
            r+=1
    answ=100000000000
    for i in ans:
        if i[0]+1 + i[1]-t1<answ:
            answ=i[0]+1 + i[1]-t1
    if answ==100000000000:
        answ=-1
    return answ




solution([3, 2, 7, 2], [4, 6, 5, 1])