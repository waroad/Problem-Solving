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
            tmp = arrF[0][:]
            arrF[0] = arrR[0][:]
            arrR[0]=arrB[0][:]
            arrB[0]=arrL[0][:]
            arrL[0]=tmp[:]
        else:
            for m in range(3):
                for n in range(3):
                    arrU[m][n]=arr_tmp[n][2-m]
            tmp = arrF[0][:]
            arrF[0] = arrL[0][:]
            arrL[0] = arrB[0][:]
            arrB[0] = arrR[0][:]
            arrR[0] = tmp[:]
    elif act[i][0]=='D':
        for m in range(3):
            arr_tmp[m] = arrD[m][:]
        if act[i][1] == '+':
            for m in range(3):
                for n in range(3):
                    arrD[m][n] = arr_tmp[2 - n][m]
            tmp = arrF[2][:]
            arrF[2] = arrL[2][:]
            arrL[2] = arrB[2][:]
            arrB[2] = arrR[2][:]
            arrR[2] = tmp[:]
        else:
            for m in range(3):
                for n in range(3):
                    arrD[m][n] = arr_tmp[n][2 - m]
            tmp = arrF[2][:]
            arrF[2] = arrR[2][:]
            arrR[2] = arrB[2][:]
            arrB[2] = arrL[2][:]
            arrL[2] = tmp[:]
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
                arrF[k][0] = tmp
        else:
            for m in range(3):
                for n in range(3):
                    arrB[m][n] = arr_tmp[n][2 - m]
            for k in range(3):
                tmp = arrU[k][0]
                arrU[k][0] = arrF[k][0]
                arrF[k][0] = arrD[2 - k][2]
                arrD[2 - k][2] = arrB[2 - k][2]
                arrB[2 - k][2] = tmp



print(act)
