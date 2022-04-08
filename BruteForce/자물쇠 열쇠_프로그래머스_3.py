# 카카오 블라인드 채용 문제. 30분 정도
# 그냥저냥 brutal force 로 2차원 배열 돌려가면서 다 대입해보는
# 문제이다. 중간에 for 구문에서 값을 하나 잘못 넣어서 30분정도 걸렸다.


def solution(key, lock):
    lock2=[x[:] for x in lock]
    for t in range(4):
        key2=[x[:] for x in key]
        for i in range(len(key)):
            for j in range(len(key)):
                key[i][j]=key2[j][len(key)-i-1]
        for a in range(len(key)-1, -len(lock),-1):
            for b in range(len(key)-1, -len(lock),-1):
                tmp=0
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        if 0<=i+a<len(key) and 0<=j+b<len(key):
                            lock[i][j]+=key[i+a][j+b]
                        if lock[i][j]!=1:
                            # for k in range(len(lock)):
                            #     print(*lock[k])
                            # print(a,b,i,j)
                            tmp=1
                            break
                        if i==len(lock)-1 and j==len(lock)-1:
                            return True
                    if tmp==1:
                        lock = [x[:] for x in lock2]
                        break

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))