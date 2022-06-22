def solution(rc, operations):
    lr=len(rc[0])
    ud=len(rc)
    ind=0
    for i in operations:
        if i=="Rotate":
            tt=rc[0-ind][:]
            for i in range(1,ud-1):
                tt.append(rc[i-ind][lr-1])
            for j in range(lr-1,-1,-1):
                tt.append(rc[ud-1-ind][j])
            for i in range(ud-2,0,-1):
                tt.append(rc[i-ind][0])
            cnt=0
            for j in range(1,lr):
                rc[0-ind][j]=tt[cnt]
                cnt+=1
            for i in range(1,ud-1):
                rc[i-ind][lr-1]=tt[cnt]
                cnt+=1
            for j in range(lr-1,-1,-1):
                rc[ud-1-ind][j]=tt[cnt]
                cnt+=1
            for i in range(ud-2,0,-1):
                rc[i-ind][0]=tt[cnt]
                cnt+=1
            rc[0-ind][0]=tt[-1]

        else:
            ind+=1
            ind%=ud
    ans=[[] for _ in range(ud)]
    for i in range(ud):
        ans[i]=rc[i-ind][:]
    return ans


solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"])