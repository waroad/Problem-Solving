import math
import matplotlib.pyplot as plt
from operator import itemgetter
circles = []
with open("input.txt", "r") as f:
    x, y = [float(x) for x in f.readline().split()]
    while True:
        circle = [float(x) for x in f.readline().split()]
        if not circle:
            break
        circles.append(circle)
for circle in circles:
    circle[0] -= x
    circle[1] -= y


def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
    h = math.sqrt(r0 ** 2 - a ** 2)
    x2 = x0 + a * (x1 - x0) / d
    y2 = y0 + a * (y1 - y0) / d
    x3 = x2 + h * (y1 - y0) / d
    y3 = y2 - h * (x1 - x0) / d

    x4 = x2 - h * (y1 - y0) / d
    y4 = y2 + h * (x1 - x0) / d

    return [x3, y3, x4, y4]


def make_arr(a, b, c):
    arr = [a, b, c]
    if a >= 0 and b >= 0:
        arr.append(1)
    elif a >= 0 and b < 0:
        arr.append(2)
    elif a<0 and b<0:
        arr.append(3)
    else:
        arr.append(4)
    if a==0 and b>=0:
        arr.append(10000000000)
    elif a==0 and b<0:
        arr.append(-10000000000)
    else:
        arr.append(b/a)
    # arr: [x, y, 원 ind, 사분면, 기울기, 왼:0오:1]
    return arr


def find(a):
    dict1={cords[a][2]:0}
    arr1=[]
    cnt=0
    ff=1
    for i in range(a,a+len(cords)):
        t=i%len(cords)
        if ff==1:
            if cords[t][5] == 1 and cords[t][2] in arr1:
                for dots in arr1:
                    dict1[dots]=0
                cnt+=1
                ff=0
                arr1=[]
            else:
                arr1.append(cords[t][2])
        else:
            if cords[t][5]==0:
                arr1.append(cords[t][2])
            elif cords[t][5]==1 and cords[t][2] not in dict1:
                cnt+=1
                for dots in arr1:
                    dict1[dots]=0
                arr1=[]
    return cnt


min_d=1000000000
min_ind=0
cords = []
for ind, circle in enumerate(circles):
    c = math.sqrt(circle[0] ** 2 + circle[1] ** 2 - circle[2]**2)
    if c <= 0:
        continue
    tmp = get_intersections(0, 0, c, circle[0], circle[1], circle[2])
    t1=make_arr(tmp[0], tmp[1], ind)
    t2 = make_arr(tmp[2], tmp[3], ind)
    d = math.sqrt((tmp[2] - tmp[0]) ** 2 + (tmp[3] - tmp[1]) ** 2)
    if d<min_d:
        min_ind=ind
        min_d=d
    t1.append(1)
    cords.append(t1)
    t2.append(0)
    cords.append(t2)
cords.sort(key=itemgetter(4),reverse=True)
cords.sort(key=itemgetter(3))
ans=1000000000
for ind,i in enumerate(cords):
    if i[2]==min_ind and i[5]==0:
        ans=find(ind)
'''
# 시각화 하기
plt.axvline(x=0, color = 'r') # draw x =0
plt.axhline(y=0, color = 'r')
plt.scatter(0,0)
colors = "bgrcmyk"
for ind,c in enumerate(cords):
    plt.scatter(c[0],c[1],c=colors[c[2]%7])
    plt.annotate(str(ind)+'-'+str(c[5]),(c[0],c[1]))
plt.show()
'''
f = open("output.txt", 'w')
f.write(str(ans))
f.close()
