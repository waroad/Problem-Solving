# 실버 1, 브루트포스, 20분.
# 넣기 좀 뭐하지만; 한 김에 넣었다.
# 코드 전체를 짜진 않았다.

from itertools import combinations

n = int(input())

answer = False

field = []
blanks = []
teachers = []
num_of_students=0
for i in range(n):
    row = list(input().split())
    for j in range(n):
        if row[j] == 'S':
            num_of_students+=1
        elif row[j] == 'X':
            blanks.append([i, j])
        elif row[j] == 'T':
            teachers.append([i, j])
    field.append(row)

standard_field = [i[:] for i in field]


def spread(a,b):
    a2=a
    b2=b
    while a+1<n and field[a+1][b]!='O':
        field[a+1][b]='T'
        a+=1
    a=a2
    while a-1>=0 and field[a-1][b]!='O':
        field[a-1][b]='T'
        a-=1
    a=a2
    while b + 1 < n and field[a][b+1] != 'O':
        field[a][b+1] = 'T'
        b+=1
    b=b2
    while b -1 >= 0 and field[a][b - 1] != 'O':
        field[a][b - 1] = 'T'
        b -= 1
    b=b2


obj_cases = list(combinations(blanks, 3))
num_of_students2=num_of_students
while obj_cases:
    num_of_students=num_of_students2
    case = obj_cases.pop()
    for i in case:
        field[i[0]][i[1]] = 'O'
    for teacher in teachers:
        spread(teacher[0],teacher[1])
    for i in range(n):
        for j in range(n):
            if field[i][j]=='S':
                num_of_students-=1
    if num_of_students==0:
        answer=True
        break
    field = [i[:] for i in standard_field]

if answer:
    print('YES')
else:
    print('NO')
