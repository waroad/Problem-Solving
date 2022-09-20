import math
import matplotlib.pyplot as plt


def grahamScan(l1):

    def ccw(i, j, k):
        area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
        if area2 > 0: return True
        else: return False

    min_ind=-1
    min_v=10000000
    for ind,i in enumerate(l1):
        if i[1]<min_v:
            min_v=i[1]
            min_ind=ind
    first_v=l1.pop(min_ind)
    l1=sorted(l1,key=lambda x: math.atan2(x[1]-first_v[1], x[0] - first_v[0]))
    print(l1)
    ans=[first_v,l1[0]]
    for i in range(1,len(l1)):
        while not ccw(ans[len(ans)-2],ans[len(ans)-1],l1[i]):
            ans.pop()
        ans.append(l1[i])
    while not ccw(ans[len(ans)-2],ans[len(ans)-1],first_v):
        ans.pop()

    print(ans)
    plt.scatter(first_v[0], first_v[1])
    plt.annotate(str("hihii"), (first_v[0], first_v[1]))
    for ind,i in enumerate(l1):
        plt.scatter(i[0],i[1])
        plt.annotate(str(ind), (i[0], i[1]))
    plt.show()

grahamScan([(4,2),(3,-1),(2,-2),(1,0),(0,2),(0,-2),(-1,1),(-2,-1),(-2,-3),(-3,3),(-4,0),(-4,-2),(-4,-4)])