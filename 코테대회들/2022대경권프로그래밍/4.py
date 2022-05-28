def solution(s,query):
    arr=[0]*len(s)
    ttt=len(s)
    ans=[]
    cnt=0
    for i in query:
        tt=i.split()
        if tt[0]=='1':
            if arr[int(tt[1])-1]==arr[int(tt[2])-1]:
                ans.append("YES")
            else:
                ans.append("NO")
        elif tt[0] == '2':
            ar=arr[int(tt[1])-1]
            cnt+=1
            for j in range(ttt):
                if arr[j]==ar:
                    if s[j] in tt[2]:
                        arr[j] = cnt
        elif tt[0]=='3':
            cnt+=1
            print(int(tt[1])-1,int(tt[2]))
            for j in range(int(tt[1])-1, int(tt[2])):
                if s[j] in tt[3]:
                    arr[j]=cnt
        elif tt[0]=='4':
            a1=arr[int(tt[1])-1]
            a2=arr[int(tt[2])-1]
            print(a1,a2)
            for j in range(ttt):
                if arr[j]==a2:
                    arr[j]=a1
        else:
            break
    return ans

print(solution("programmers",["1 1 5", "2 1 rm", "1 1 5", "5"]))

print(solution("abacadae", ["3 1 4 a", "1 1 5", "4 1 7", "1 1 5", "5"]))