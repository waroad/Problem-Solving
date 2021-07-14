import sys
n, s, d=[int(x) for x in input().split()]
arr=[[] for i in range(n)]
arrL=[0]*n


def loop(a,b,c):
    for i in range(len(arr[a])):
        if arr[a][i]!=b:
            print(arr[a][i],c+1)
            loop(arr[a][i],a,c+1)


for i in range(n-1):
    temp=[int(x) for x in sys.stdin.readline().split()]
    arr[temp[0]-1].append(temp[1]-1)
    arr[temp[1]-1].append(temp[0]-1)
    arrL[temp[0]-1]+=1
    arrL[temp[1]-1]+=1

print(arr)
print(arrL)
loop(s-1,-1,0)





