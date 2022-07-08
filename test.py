room_size, hint_num = [int(x) for x in input().split()]
arr=[[int(x) for x in input().split()] for _ in range(room_size)]

hint_coord=[[] for _ in range(hint_num)]
for i in range(room_size):
    for j in range(room_size):
        if arr[i][j]!=0:
            hint_coord[arr[i][j]-1]=[i,j]
ans=0
for i in range(1,hint_num):
    ans+=abs(hint_coord[i][0]-hint_coord[i-1][0]) + abs(hint_coord[i][1]-hint_coord[i-1][1])

print(ans)