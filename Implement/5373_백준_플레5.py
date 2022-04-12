# 플레 5, 구현, 1시간 10분 정도
# 오랫만에 완전 내 힘으로 플레 문제를 맞추었다! 기분이 좋다.
# 구현 문제라서 머릿속으로 생각한 것을 그대로 짜면 되는 문제인데,
# 이게 또 큐브 전개도 문제라 내가 이런쪽으로 강해 풀 수 있었다.
# 큐브를 돌리는 걸 시뮬레이트 해서 저장하고 그걸 나중에 출력하는 문제다.


T=int(input())
for z in range(T):
    n=int(input())
    act=[x for x in input().split()]
    arrU=[["w","w","w"],["w","w","w"],["w","w","w"]]
    arrD=[["y","y","y"],["y","y","y"],["y","y","y"]]
    arrF=[["r","r","r"],["r","r","r"],["r","r","r"]]
    arrB=[["o","o","o"],["o","o","o"],["o","o","o"]]
    arrL=[["g","g","g"],["g","g","g"],["g","g","g"]]
    arrR=[["b","b","b"],["b","b","b"],["b","b","b"]]

    for i in range(n):
        arr_tmp = [[] for _ in range(3)]
        if act[i][0]=='U':
            for m in range(3):
                arr_tmp[m] = arrU[m][:]
            if act[i][1]=='+':
                for m in range(3):
                    for n in range(3):
                        arrU[m][n]=arr_tmp[2-n][m]
                for k in range(3):
                    tmp = arrF[0][k]
                    arrF[0][k] = arrR[0][k]
                    arrR[0][k] = arrB[0][k]
                    arrB[0][k] = arrL[0][k]
                    arrL[0][k] = tmp
            else:
                for m in range(3):
                    for n in range(3):
                        arrU[m][n]=arr_tmp[n][2-m]
                for k in range(3):
                    tmp=arrF[0][k]
                    arrF[0][k]=arrL[0][k]
                    arrL[0][k]=arrB[0][k]
                    arrB[0][k]=arrR[0][k]
                    arrR[0][k]=tmp
        elif act[i][0]=='D':
            for m in range(3):
                arr_tmp[m] = arrD[m][:]
            if act[i][1] == '+':
                for m in range(3):
                    for n in range(3):
                        arrD[m][n] = arr_tmp[2 - n][m]
                for k in range(3):
                    tmp = arrF[2][k]
                    arrF[2][k] = arrL[2][k]
                    arrL[2][k] = arrB[2][k]
                    arrB[2][k] = arrR[2][k]
                    arrR[2][k] = tmp
            else:
                for m in range(3):
                    for n in range(3):
                        arrD[m][n] = arr_tmp[n][2 - m]
                for k in range(3):
                    tmp = arrF[2][k]
                    arrF[2][k] = arrR[2][k]
                    arrR[2][k] = arrB[2][k]
                    arrB[2][k] = arrL[2][k]
                    arrL[2][k] = tmp
        elif act[i][0] == 'F':
            for m in range(3):
                arr_tmp[m] = arrF[m][:]
            if act[i][1] == '+':
                for m in range(3):
                    for n in range(3):
                        arrF[m][n] = arr_tmp[2 - n][m]
                for k in range(3):
                    tmp=arrU[2][k]
                    arrU[2][k] = arrL[2-k][2]
                    arrL[2-k][2] = arrD[2][k]
                    arrD[2][k] = arrR[k][0]
                    arrR[k][0]= tmp
            else:
                for m in range(3):
                    for n in range(3):
                        arrF[m][n] = arr_tmp[n][2 - m]
                for k in range(3):
                    tmp=arrU[2][k]
                    arrU[2][k] = arrR[k][0]
                    arrR[k][0] = arrD[2][k]
                    arrD[2][k] = arrL[2 - k][2]
                    arrL[2 - k][2] = tmp
        elif act[i][0] == 'L':
            for m in range(3):
                arr_tmp[m] = arrL[m][:]
            if act[i][1] == '+':
                for m in range(3):
                    for n in range(3):
                        arrL[m][n] = arr_tmp[2 - n][m]
                for k in range(3):
                    tmp=arrU[k][0]
                    arrU[k][0] = arrB[2-k][2]
                    arrB[2-k][2] = arrD[2-k][2]
                    arrD[2-k][2] = arrF[k][0]
                    arrF[k][0]= tmp
            else:
                for m in range(3):
                    for n in range(3):
                        arrL[m][n] = arr_tmp[n][2 - m]
                for k in range(3):
                    tmp = arrU[k][0]
                    arrU[k][0] = arrF[k][0]
                    arrF[k][0] = arrD[2 - k][2]
                    arrD[2 - k][2] = arrB[2 - k][2]
                    arrB[2 - k][2] = tmp
        elif act[i][0] == 'B':
            for m in range(3):
                arr_tmp[m] = arrB[m][:]
            if act[i][1] == '+':
                for m in range(3):
                    for n in range(3):
                        arrB[m][n] = arr_tmp[2 - n][m]
                for k in range(3):
                    tmp = arrU[0][2-k]
                    arrU[0][2-k] = arrR[2-k][2]
                    arrR[2-k][2] = arrD[0][2-k]
                    arrD[0][2-k]= arrL[k][0]
                    arrL[k][0] = tmp
            else:
                for m in range(3):
                    for n in range(3):
                        arrB[m][n] = arr_tmp[n][2 - m]
                for k in range(3):
                    tmp = arrU[0][2 - k]
                    arrU[0][2 - k] = arrL[k][0]
                    arrL[k][0] = arrD[0][2 - k]
                    arrD[0][2 - k] = arrR[2 - k][2]
                    arrR[2 - k][2] = tmp
        elif act[i][0] == 'R':
            for m in range(3):
                arr_tmp[m] = arrR[m][:]
            if act[i][1] == '+':
                for m in range(3):
                    for n in range(3):
                        arrR[m][n] = arr_tmp[2 - n][m]
                for k in range(3):
                    tmp = arrU[2-k][2]
                    arrU[2-k][2] = arrF[2 - k][2]
                    arrF[2 - k][2] = arrD[k][0]
                    arrD[k][0] = arrB[k][0]
                    arrB[k][0] = tmp
            else:
                for m in range(3):
                    for n in range(3):
                        arrR[m][n] = arr_tmp[n][2 - m]
                for k in range(3):
                    tmp = arrU[2-k][2]
                    arrU[2-k][2]= arrB[k][0]
                    arrB[k][0] = arrD[k][0]
                    arrD[k][0] = arrF[2 - k][2]
                    arrF[2 - k][2] = tmp

    for i in range(3):
        print(arrU[i][0],end='')
        print(arrU[i][1],end='')
        print(arrU[i][2])
    # print("")
    # for i in range(3):
    #     print(*arrD[i])
    # print("")
    # for i in range(3):
    #     print(*arrF[i],end='  ')
    #     print(*arrR[i],end='  ')
    #     print(*arrB[i],end='  ')
    #     print(*arrL[i],end='  ')
    #     print("")
    # print("")
