def solution(line):
    l=[1,0]
    r=[1,9]
    ans=[]
    dict1={"Q":[1,0],"W":[1,1],"E":[1,2],"R":[1,3],"T":[1,4],"Y":[1,5],"U":[1,6],"I":[1,7],"O":[1,8],"P":[1,9],
           "1":[0,0],"2":[0,1],"3":[0,2],"4":[0,3],"5":[0,4],"6":[0,5],"7":[0,6],"8":[0,7],"9":[0,8],"0":[0,9]}
    left=["Q","W","E","R","1","2","3","4","5","T"]
    for letter in line:
        L=abs(l[0]-dict1[letter][0])+abs(l[1]-dict1[letter][1])
        R=abs(r[0]-dict1[letter][0])+abs(r[1]-dict1[letter][1])
        if L<R:
            ans.append(0)
            l=dict1[letter]
        elif R<L:
            ans.append(1)
            r=dict1[letter]
        else:
            print("wow1",letter)
            L = abs(l[1] - dict1[letter][1])
            R = abs(r[1] - dict1[letter][1])
            print(L,R)
            if L < R:
                ans.append(0)
                l = dict1[letter]
            elif R < L:
                ans.append(1)
                r = dict1[letter]
            else:
                print("wow")
                if letter in left:
                    ans.append(0)
                    l = dict1[letter]
                else:
                    ans.append(1)
                    r=dict1[letter]
    return ans




solution("Q4OYPI")