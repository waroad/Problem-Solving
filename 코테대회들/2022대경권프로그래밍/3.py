ans=10000
def solution(grid):
    global ans
    arr=[[[0 for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    w=len(grid[0])
    h=len(grid)
    ans=100000000

    def find(y,x,dir,move,c):
        global ans
        move+=1
        print(y,x,dir,move,c)
        if y==h-1 and x==w-1:
            ans=min(ans,move-1)
            return
        if arr[y][x][dir]== 0 or move<arr[y][x][dir]:
            arr[y][x][dir] = move
        else:
            return
        if dir==1:
            if x+1<w and grid[y][x+1]=='.':
                find(y,x+1,dir,move,0)
            if c<2:
                find(y,x,0,move,c+1)
        elif dir==2:
            if y+1<h and grid[y+1][x]=='.':
                find(y+1,x,dir,move,0)
            if c<2:
                find(y,x,1,move,c+1)
        elif dir==3:
            if x>0 and grid[y][x-1]=='.':
                find(y,x-1,dir,move,0)
            if c<2:
                find(y,x,2,move,c+1)
        else:
            if y>0 and grid[y-1][x]=='.':
                find(y-1,x,dir,move,0)
            if c<2:
                find(y,x,3,move,c+1)

    find(0,0,1,0,0)
    return ans


print(solution(["...", "#.#", "..#", "#.."]))
print(solution(["..#..", ".#...", ".#...", "...#."]))