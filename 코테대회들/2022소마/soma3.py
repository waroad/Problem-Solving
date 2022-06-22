a,b=[int(x) for x in input().split()]
str=input()
for k in str:
    t=ord(k)-97-b
    while t%a!=0:
        t+=26
    print(chr(t//a+97),end='')