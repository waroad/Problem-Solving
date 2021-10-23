# 플레 5, dp, 1시간 반 정도
# 일단 맞추긴 했는데, 다른 방법을 몇개 훑어 보니
# 꽤나 비효율 적인 방법인 것 같다. 나는 dict 의 key 값에 접근하는 것이
# O(1) 밖에 안걸린다는 것에 착안해, 현재 경찰차의 좌표들을 string 으로 변환해서
# key 로 사용해서 풀었는데, 2차원 dp 배열로 충분히 조금 더 빠르게 풀 수 있는 문제였다.
# 그래도 뭐 일단 맞춘것에 만족한다. 이제는 확실히 전보다는 문제를 더 잘 푸는 것 같다.
# 그리디 플레 5는 그래도 꽤 풀었고, dp 도 오늘 풀었으니 앞으로 dp 골드 1, 플레 5
# 언저리 조금 더 하다가, 그래프, 비트마스킹 으로 넘어가 봐야겠다. 


N = int(input())
W = int(input())
arr = [[int(x) for x in input().split()] for _ in range(W)]
greed = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
arr2 = []
dict1 = {}
dict2 = {}
dict1['1 1 ' + str(N) + ' ' + str(N)] = [0, '']
for ind, i in enumerate(arr):
    if ind % 2 == 0:
        for keys in dict1:
            temp = keys.split()
            car1 = [int(temp[0]), int(temp[1])]
            car2 = [int(temp[2]), int(temp[3])]
            acc = dict1[keys][0]
            if str(i[0]) + ' ' + str(i[1]) + ' ' + str(car2[0]) + ' ' + str(car2[1]) not in dict2 or \
                    abs(i[0] - car1[0]) + abs(i[1] - car1[1]) + acc < \
                    dict2[str(i[0]) + ' ' + str(i[1]) + ' ' + str(car2[0]) + ' ' + str(car2[1])][0]:
                dict2[str(i[0]) + ' ' + str(i[1]) + ' ' + str(car2[0]) + ' ' + str(car2[1])] = [
                    abs(i[0] - car1[0]) + abs(i[1] - car1[1]) + acc, dict1[keys][1] + '1']
            if str(car1[0]) + ' ' + str(car1[1]) + ' ' + str(i[0]) + ' ' + str(i[1]) not in dict2 or \
                    abs(i[0] - car2[0]) + abs(i[1] - car2[1]) + acc < \
                    dict2[str(car1[0]) + ' ' + str(car1[1]) + ' ' + str(i[0]) + ' ' + str(i[1])][0]:
                dict2[str(car1[0]) + ' ' + str(car1[1]) + ' ' + str(i[0]) + ' ' + str(i[1])] = [
                    abs(i[0] - car2[0]) + abs(i[1] - car2[1]) + acc, dict1[keys][1] + '2']
        dict1 = {}
    else:
        for keys in dict2:
            temp = keys.split()
            car1 = [int(temp[0]), int(temp[1])]
            car2 = [int(temp[2]), int(temp[3])]
            acc = dict2[keys][0]
            if str(i[0]) + ' ' + str(i[1]) + ' ' + str(car2[0]) + ' ' + str(car2[1]) not in dict1 or \
                    abs(i[0] - car1[0]) + abs(i[1] - car1[1]) + acc < \
                    dict1[str(i[0]) + ' ' + str(i[1]) + ' ' + str(car2[0]) + ' ' + str(car2[1])][0]:
                dict1[str(i[0]) + ' ' + str(i[1]) + ' ' + str(car2[0]) + ' ' + str(car2[1])] = [
                    abs(i[0] - car1[0]) + abs(i[1] - car1[1]) + acc, dict2[keys][1] + '1']
            if str(car1[0]) + ' ' + str(car1[1]) + ' ' + str(i[0]) + ' ' + str(i[1]) not in dict1 or \
                    abs(i[0] - car2[0]) + abs(i[1] - car2[1]) + acc < \
                    dict1[str(car1[0]) + ' ' + str(car1[1]) + ' ' + str(i[0]) + ' ' + str(i[1])][0]:
                dict1[str(car1[0]) + ' ' + str(car1[1]) + ' ' + str(i[0]) + ' ' + str(i[1])] = [
                    abs(i[0] - car2[0]) + abs(i[1] - car2[1]) + acc, dict2[keys][1] + '2']
        dict2 = {}
if W % 2 == 1:
    ans = min(dict2, key=dict2.get)
    print(dict2[ans][0])
    print(*list(dict2[ans][1]), sep='\n')
else:
    ans = min(dict1, key=dict1.get)
    print(dict1[ans][0])
    print(*list(dict1[ans][1]), sep='\n')
