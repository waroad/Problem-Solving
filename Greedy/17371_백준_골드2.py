n=int(input())
arr=[]
for i in range(n):
    tmp=[int(x) for x in input().split()]
    arr.append([2*tmp[0],2*tmp[1],tmp[0]*tmp[0]+tmp[1]*tmp[1]])

print(arr)
