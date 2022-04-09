# 퍼즐 조각 채우기 푸는 중, 시간이 늦어서 내일 끝내기로
def solution(game_board, table):
    components = []
    components2 = []

    def cut(a, b, board, components_selected):
        board[a][b] = 0
        tmp=components_selected[len(components_selected) - 1][len(components_selected[len(components_selected) - 1]) - 1]
        if a + 1 < len(table) and board[a + 1][b] == 1:
            components_selected[len(components_selected) - 1].append([tmp[0] + 1, tmp[1]])
            cut(a + 1, b, board, components_selected)
        if b + 1 < len(table[0]) and board[a][b + 1] == 1:
            components_selected[len(components_selected) - 1].append([tmp[0], tmp[1] + 1])
            cut(a, b + 1, board, components_selected)
        if b > 0 and board[a][b - 1] == 1:
            components_selected[len(components_selected) - 1].append([tmp[0], tmp[1] - 1])
            cut(a, b - 1, board, components_selected)

    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 1:
                components.append([[0, 0]])
                cut(i, j, table, components)
    for i in range(len(table)):
        for j in range(len(table[0])):
            game_board[i][j]=(game_board[i][j]+1)//2
    for i in range(len(table)):
        for j in range(len(table[0])):
            if game_board[i][j] == 1:
                components2.append([[0, 0]])
                cut(i, j, game_board, components2)
    components.sort()
    components2.sort()
    for i in components:
        print(i)
    print("")
    for i in components2:
        print(i)
    answer = -1

    for i in components:

    return answer


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0]]))
