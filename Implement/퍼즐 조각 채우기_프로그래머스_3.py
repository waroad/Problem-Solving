# 1시간 가량, 구현과 dfs brutal force 문제.
# 주는 점수를 보아 3단계 중에는 어려운 편인 것 같다.
# 이것도 원래 조금 더 빨리 풀 수 있었는데, 2차원 배열에서 연결되어 있는 조각을 탐색할 때,
# 위로 가는 경우, 즉 arr[a-1][b] 을 찾는 경우를 고려를 안해서 2개 테스트 케이스가 계속 틀려 그걸 찾느라 시간이 좀 걸렸다.
# 이런 구현 문제도 오랫만에 또 풀어봐서 좋았다. 코드가 좀 길고 더럽긴 하네;
def solution(game_board, table):
    components = []
    components2 = []

    def cut(a, b, board, components_selected):
        board[a][b] = 0
        cur_cor=components_selected[len(components_selected) - 1][len(components_selected[len(components_selected) - 1]) - 1]
        if a + 1 < len(table) and board[a + 1][b] == 1:
            components_selected[len(components_selected) - 1].append([cur_cor[0] + 1, cur_cor[1]])
            cut(a + 1, b, board, components_selected)
        if a > 0 and board[a - 1][b] == 1:
            components_selected[len(components_selected) - 1].append([cur_cor[0] - 1, cur_cor[1]])
            cut(a - 1, b, board, components_selected)
        if b + 1 < len(table[0]) and board[a][b + 1] == 1:
            components_selected[len(components_selected) - 1].append([cur_cor[0], cur_cor[1] + 1])
            cut(a, b + 1, board, components_selected)
        if b > 0 and board[a][b - 1] == 1:
            components_selected[len(components_selected) - 1].append([cur_cor[0], cur_cor[1] - 1])
            cut(a, b - 1, board, components_selected)

    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 1:
                components.append([[0, 0]])
                cut(i, j, table, components)
    for i in range(len(table)):
        for j in range(len(table[0])):
            game_board[i][j]=(game_board[i][j]+1)%2
    for i in range(len(table)):
        for j in range(len(table[0])):
            if game_board[i][j] == 1:
                components2.append([[0, 0]])
                cut(i, j, game_board, components2)
    components.sort()
    components2.sort()
    ans = 0
    components_dict={}
    for i in components:
        tmp = [x[:] for x in i]
        for j in range(4):
            tmp2=[]
            for k in tmp:
                tmp2.append([k[1],-k[0]])
            tmp = [x[:] for x in tmp2]
            dy=0
            dx=0
            for a in tmp:
                if a[0]<dy:
                    dy=a[0]
                if a[1]<dx:
                    dx=a[1]
            for a in tmp:
                a[0]-=dy
                a[1]-=dx
            tmp.sort()
            if str(tmp) in components_dict:
                components_dict[str(tmp)]+=1
                break
            if j == 3:
                components_dict[str(tmp)]=1
    for i in components2:
        tmp = [x[:] for x in i]
        for j in range(4):
            tmp2=[]
            for k in tmp:
                tmp2.append([k[1],-k[0]])
            tmp = [x[:] for x in tmp2]
            dy=0
            dx=0
            for a in tmp:
                if a[0]<dy:
                    dy=a[0]
                if a[1]<dx:
                    dx=a[1]
            for a in tmp:
                a[0]-=dy
                a[1]-=dx
            tmp.sort()
            if str(tmp) in components_dict and components_dict[str(tmp)]>0:
                components_dict[str(tmp)]-=1
                ans+=len(tmp)
                break
    return ans


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0]]))
