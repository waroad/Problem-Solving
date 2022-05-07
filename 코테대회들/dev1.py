import operator
def solution(dist):
    answer = []
    aa=[[] for _ in range(2)]
    ans1= {}
    ans1[0]=100000001
    ans1[1]=ans1[0]-dist[1][0]
    for i in range(2,len(dist)):
        tmp=ans1[i-1]-dist[i][i-1]
        if dist[i][i-2]==abs(ans1[i-2]-tmp):
            ans1[i]=tmp
        else:
            ans1[i]=ans1[i-1]+dist[i][i-1]
    sorted_x = sorted(ans1.items(), key=operator.itemgetter(1))
    for i in range(len(dist)):
        answer.append(sorted_x[i][0])
        aa[0].append(sorted_x[i][0])
    answer.reverse()
    for i in answer:
        aa[1].append(i)
    aa.sort()
    return aa





print(solution([[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]))