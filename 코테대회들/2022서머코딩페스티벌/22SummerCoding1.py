def solution(atmos):
    cnt=0
    done=0
    used=0
    for i in atmos:
        if i[0]>150 and i[1]>75:
            if done:
                used=0
                done=0
            else:
                cnt+=1
                done=0
                used=0
        elif i[0]>80 or i[1]>35:
            if not done:
                cnt+=1
                done=1
                used=0
        if done:
            used+=1
            if used>=3:
                used=0
                done=0
        print(i,cnt,done,used)
    return cnt


solution([[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]])



