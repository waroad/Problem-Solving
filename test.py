# 플레 2, 분할 정복 2시간 하고 못풀고 풀이 봄
# 이게 학교 과제로 나와서 플레 2라 조금 높은 감은 있었는데, 역시는 역시다.
# 설명 없이 하려니 어렵네..
# 근데 학교 과제는 여기서 시간을 한번 더 단축하는 것이어서, 최소 플레 2의
# 난이도다. 일단은 풀어보려고 한다.
import sys
from bisect import bisect_left, bisect_right
from collections import deque


class KeyWrapper:
    def __init__(self, iterable, key):
        self.it = iterable
        self.key = key

    def __getitem__(self, i):
        return self.key(self.it[i])

    def __len__(self):
        return len(self.it)


n=int(input())
arr=[[int(x)+10000 for x in sys.stdin.readline().split()] for _ in range(n)]
arr.sort(key = lambda x: x[0])
dist=(arr[0][0]-arr[1][0])**2 + (arr[0][1]-arr[1][1])**2
deq= deque()
deq.append(arr[0])
deq.append(arr[1])
x_set=[arr[0],arr[1]]
x_set.sort(key=lambda x: x[1])
for i in range(2,n):
    c = []
    while len(deq) and (deq[0][0] - arr[i][0]) ** 2 > dist:
        x_set.remove(deq[0])
        deq.popleft()
    if len(deq)==0:
        deq.append(arr[i])
        bslindex = bisect_left(KeyWrapper(x_set, key=lambda c: c[1]), arr[i][1])
        x_set.insert(bslindex, arr[i])
        continue
    tt=arr[i][1]
    l = bisect_right(KeyWrapper(x_set, key=lambda c: c[1]), arr[i][1]-dist**0.5)
    h = bisect_left(KeyWrapper(x_set, key=lambda c: c[1]), arr[i][1]+dist**0.5)
    deq.append(arr[i])
    bslindex = bisect_left(KeyWrapper(x_set, key=lambda c: c[1]), arr[i][1])
    x_set.insert(bslindex, arr[i])
    for j in range(l,h):
        dist = min(dist, (x_set[j][0] - arr[i][0]) ** 2 + (x_set[j][1] - arr[i][1]) ** 2)
print(dist)