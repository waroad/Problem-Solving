# 플레 5, 그리디, 1시간 좀 안되게
# 일단 짜는 것 자체는 간단했다. 그냥 저냥 생각해보면 나올 수 있는 정도의 사고를 요구한다.
# 그리고 다른사람들은 어떻게 짰나 봤는데, 누구 한명이 3줄만에 짰길래 확실히 파이썬도
# 아직 내가 모르는 문법이 많구나 했다. 정말 파이썬은 압축이 가능한 것 같다.
# 오늘 enumerate 가 index 를 포함해서 list comprehension 을 할 수 있고,
# append 와 비슷하지만 대괄호 없이 더 할 수 있는 extend 도 알았고,
# extend 10 번 했던 것을 lambda 로 1 줄만에 할 수 있다는 것도 알았고,
# ''.join 을 통해 배열 안에 있는 char 혹은 string 값을 1줄 만에 다 더해서
# 출력할 수도 있다는 것도 알았다.
n=int(input())
arr=[list(str(x)) for x in input().split()]
arr2=[]
for ind,i in enumerate(arr):
    tmp=(lambda x: x*10)(i)
    # for j in range(10):
    #     tmp.extend(i)
    tmp=tmp[:10]
    tmp.append(ind)
    arr2.append(tmp)
arr2.sort(reverse=True)
ans=[]
for i in range(n):
    ans.extend(arr[arr2[i][10]])
print(ans)
print(int(''.join(ans)))
