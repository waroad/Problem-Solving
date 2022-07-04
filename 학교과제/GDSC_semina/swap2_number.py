def swap2(a,b):
    tmp=a
    a=b
    b=tmp
    print("로컬 a id:",id(a), "\n로컬 a 값:", a, "\n로컬 b id:",id(b), "\n로컬 b 값:",b, end="\n\n")
    return a,b


value1=20
value2=50
print("value1 id:",id(value1), "\nvalue1 값:", value1, "\nvalue2 id:",id(value2),
      "\nvalue2 값:",value2,end="\n\n")
value1,value2=swap2(value1, value2)
print("value1 id:",id(value1), "\nvalue1 값:", value1, "\nvalue2 id:",id(value2),
      "\nvalue2 값:",value2,end="\n\n")
