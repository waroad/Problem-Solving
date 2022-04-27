# 카카오 2018 공채에서 7문제 중 2번째로 정답률이 낮은 문제다.
# 그거 치고는 쉬운 편이었고, 30분 쫌 안걸렸던 것 같다.
# 카카오는 str 을 다루는걸 좋아하는 것 같은데, str 을 잘 변환해서 모든 경우의 수를
# 따져주면 되는 문제이다.
def solution(n, t, m, timetable):
    arr=[int(timetable[i][:2])*60 + int(timetable[i][3:]) for i in range(len(timetable))]
    cur=540
    ind=0
    ans=0
    kk=0
    arr.sort()
    for i in range(n):
        for j in range(m):
            if ind==len(arr):
                kk=1
                break
            if arr[ind]<=cur:
                ind+=1
            else:
                ans=cur
        cur+=t
    cur-=t
    # 모든 승객이 타고 버스가 남거나, 아니면 아무 승객도 못탔거나, 아니면 승객이 남았는데 버스보다 너무 느리거나
    if kk or ind==0 or ans==cur:
        return "{:02d}:{:02d}".format(cur//60, cur%60)
    # 그 외 중간에 끊기는 경우
    return "{:02d}:{:02d}".format((arr[ind-1]-1)//60, (arr[ind-1]-1)%60)


print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))