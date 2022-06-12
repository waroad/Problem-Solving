from collections import deque


def solution(grid, k):
    answer = -1
    dp=[[[100000000 for _ in range(k+1)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    height=len(grid)
    width=len(grid[0])
    deq= deque()

    deq.append([0,0,0,0])
    while deq:
        a,b,camp,move=deq.popleft()
        if dp[a][b][move]>camp and camp<min(dp[a][b][:move+1]):
            dp[a][b][move]=camp
            if grid[a][b]=='.':
                deq.append([a, b, camp+1, 0])
            if move<k:
                if a+1<height and grid[a+1][b]!='#':
                    deq.append([a+1,b,camp,move+1])
                if b+1<width and grid[a][b+1]!='#':
                    deq.append([a,b+1,camp,move+1])
                if a>0 and grid[a-1][b]!='#':
                    deq.append([a-1,b,camp,move+1])
                if b>0 and grid[a][b-1]!='#':
                    deq.append([a,b-1,camp,move+1])

    print(min(dp[height-1][width-1]))
    return answer


print(solution([".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"], 3))
