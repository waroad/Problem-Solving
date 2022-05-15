import copy
import math
import matplotlib.pyplot as plt
from operator import itemgetter
circles = []
with open("input3.txt", "r") as f:
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
    elif a >= 0 > b:
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
    # arr: [x좌표, y좌표, 원 ind, 사분면, 기울기, 시계방향 기준 먼저 나오는 접점이면:0, 아니면:1]
    return arr


def find(a,offset,b):
    dict1={}
    arr1=copy.deepcopy(b)
    cnt=0
    first_case=1
    tmp_cnt=10000000
    for i in range(a+offset,a+len(cords)):
        t=i%len(cords)
        if first_case==1:
            if cords[t][5] == 1:
                # 재귀를 거는 이유는, 첫번째 원의 두 접점 사이에 마지막 원의 나중 나오는 접점이 끼어있을 경우,
                # 사이에 껴있는 접점에 첫번째 접선을 긋는 경우와, 사이에 껴있는 접점을 무시하고 그 원은
                # 마지막에 터트리는 경우 중 어느 것이 최소일지 모르기에, 둘다 하고 비교했다.
                if cords[t][2] not in arr1:
                    tmp_cnt=find(a,(i-a)%len(cords)+1,arr1)
                dict1[cords[t][2]]=0
                for dot in arr1:
                    dict1[dot]=0
                cnt+=1
                first_case=0
                arr1={}
                used_lines.append([cords[t][0],cords[t][1]])
            else:
                arr1[cords[t][2]]=0
        else:
            if cords[t][5]==0 or (cords[t][5]==1 and cords[t][2] not in arr1 and cords[t][2] not in dict1):
                arr1[cords[t][2]]=0
            elif cords[t][5]==1 and cords[t][2] not in dict1:
                cnt+=1
                for dot in arr1:
                    dict1[dot]=0
                arr1= {}
                used_lines.append([cords[t][0],cords[t][1]])
        if t==a-1 and len(arr1)>0:
            for j in arr1:
                if j not in dict1:
                    cnt+=1
                    break
    return min(cnt,tmp_cnt)


used_lines=[]
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
cords.sort(key=itemgetter(5))
cords.sort(key=itemgetter(4),reverse=True)
cords.sort(key=itemgetter(3))
for ind,i in enumerate(cords):
    if i[5]==0 and min_ind==i[2]:
        ans=find(ind,0,{})
        break
# # 접점들 시각화하기
# plt.axvline(x=0, color = 'r') # draw x =0
# plt.axhline(y=0, color = 'r')
# plt.scatter(0,0)
# colors = "bgrcmyk"
# for ind,c in enumerate(cords):
#     plt.scatter(c[0],c[1],c=colors[c[2]%7])
#     plt.annotate(str(ind)+'-'+str(c[5]),(c[0],c[1]))
#
# 원과 접선들 시각화하기인데, 여러개 중첩되서 그려집니다. 이대로만 하면 안되고, 최솟값만 그리도록 조금 수정해야합니다.
figure, axes = plt.subplots()
for i in circles:
    a=plt.Circle((i[0],i[1]),i[2],fill=False)
    axes.add_artist(a)
for i in used_lines:
    plt.plot([0,i[0]*10],[0,i[1]*10])
plt.xlim([-80,80])
plt.ylim([-80,80])
plt.show()
f = open("output.txt", 'w')
f.write(str(ans))
f.close()
