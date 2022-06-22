from operator import itemgetter


def solution(rooms, target):
    dict1={}
    for room in rooms:
        tt=room.split("]")
        t1=int(tt[0][1:])
        t2=tt[1].split(",")
        for person in t2:
            if person not in dict1:
                dict1[person]=[t1]
            else:
                dict1[person].append(t1)
    arr=[]
    for i in dict1:
        tmp_min=1000000
        for r in dict1[i]:
            tmp_min=min(tmp_min,abs(r-target))
        arr.append([tmp_min,i,len(dict1[i])])
    arr.sort(key=itemgetter(1))
    arr.sort(key=itemgetter(0))
    arr.sort(key=itemgetter(2))
    ans=[]
    for ind,a in enumerate(arr):
        if a[0]!=0:
            ans.append(a[1])
    return ans

solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"], 403)