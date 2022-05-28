def solution(h,k, boxes):
    boxes.sort()
    cur_h=0
    cur=0
    cnt=0
    while cur+1<len(boxes):
        if cur_h+k>=h:
            return cnt
        if boxes[cur]-cur_h <= k < boxes[cur + 1] - cur_h:
            cur_h=boxes[cur]
            cnt+=1
            cur+=1
        elif boxes[cur]-cur_h>k:
            return -1
        else:
            cur+=1
    print(cur,cnt,cur_h,k,h)
    print(cur_h+k,boxes[-1])
    if cur_h+k>=h:
        return cnt
    elif cur_h+k>=boxes[-1] and boxes[-1]+k>=h:
        return cnt+1
    else:
        return -1


print(solution(20, 18, [3]))

print(solution(10, 1, [9, 8, 6,7, 5, 4, 3, 2, 1]))

print(solution(12, 3, [2, 3, 6, 7, 8, 10, 11]))


