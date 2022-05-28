def solution(n, queries):
    arr=[0]*n
    arr2=[0]*n
    dict1={}
    ans=[]
    for i in queries:
        tmp=i.split()
        if tmp[1]=='request':
            if tmp[0] in dict1:
                if arr[dict1[tmp[0]]]==0:
                    arr[dict1[tmp[0]]]=1
                    tt=" 192.168.0."+str(dict1[tmp[0]]+1)
                    ans.append(tmp[0]+tt)
                else:
                    for j in range(len(arr)):
                        if arr2[j] == 0:
                            arr2[j] = 1
                            arr[j]=1
                            dict1[tmp[0]] = j
                            tt = " 192.168.0." + str(j + 1)
                            ans.append(tmp[0] + tt)
                            break
                    for j in range(len(arr)):
                        if arr[j] == 0:
                            arr[j] = 1
                            dict1[tmp[0]] = j
                            tt = " 192.168.0." + str(j + 1)
                            ans.append(tmp[0] + tt)
                            break
                        if j == len(arr) - 1:
                            ans.append(tmp[0] + ' reject')
            else:
                for j in range(len(arr)):
                    if arr[j] == 0:
                        arr[j] = 1
                        dict1[tmp[0]] = j
                        tt = " 192.168.0." + str(j + 1)
                        ans.append(tmp[0] + tt)
                        break
                    if j == len(arr) - 1:
                        ans.append(tmp[0] + ' reject')
        else:
            arr[dict1[tmp[0]]] = 0
        print(ans)

    return ans



print(solution(2, ["desktop1 request", "desktop2 request", "desktop3 request", "desktop3 request", "desktop1 release", "desktop3 request"]))



