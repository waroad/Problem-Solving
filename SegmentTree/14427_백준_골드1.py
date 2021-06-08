# 골드 1, 1시간 가량, 세그먼트 트리 문제.
# 세그먼트 트리의 제일 기본형, 그냥 전체 값중 최솟 값이 있는 index 구하기 이다.
# 전에도 풀어봤던 거라 쉽게 풀리겠지 했는데, 2차원 배열을 카피하는 과정에서
# deepcopy 를 안하고 그냥 copy 를 해서 배열이 다 연결이 되는 바람에
# 시간을 30분 정도 버렸다. 앞으로 세그먼트 트리를 조금 풀어봐야겠다.
import sys
N = int(input())
arr = [int(x) for x in input().split()]
M = int(input())
tree = [[0 for i in range(2)]for j in range(N*2+1)]
for i in range(N, N * 2):
    tree[i] = [arr[i - N], i - N + 1]
for i in range(N - 1, 0, -1):
    tree[i][0] = tree[i * 2+1][0]
    tree[i][1] = tree[i * 2+1][1]
    if tree[i * 2][0] == tree[i * 2 + 1][0]:
        tree[i][1] = min(tree[i * 2][1], tree[i * 2 + 1][1])
    if tree[i * 2][0] < tree[i * 2 + 1][0]:
        tree[i][0] = tree[i * 2][0]
        tree[i][1] = tree[i * 2][1]


def change(a, b):
    tmp_in = N + a-1
    tree[tmp_in][0] = b
    while tmp_in >= 2:
        tmp_in //= 2
        tree[tmp_in][0] = tree[tmp_in * 2 + 1][0]
        tree[tmp_in][1] = tree[tmp_in * 2 + 1][1]
        if tree[tmp_in * 2][0] == tree[tmp_in * 2 + 1][0]:
            tree[tmp_in][1]=min(tree[tmp_in * 2][1], tree[tmp_in * 2 + 1][1])
        elif tree[tmp_in * 2][0] < tree[tmp_in * 2 + 1][0]:
            tree[tmp_in][0] = tree[tmp_in * 2 ][0]
            tree[tmp_in][1] = tree[tmp_in * 2 ][1]


for i in range(M):
    tmp = [int(x) for x in sys.stdin.readline().split()]
    if tmp[0] == 2:
        sys.stdout.write(str(tree[1][1])+'\n')
    else:
        change(tmp[1], tmp[2])
