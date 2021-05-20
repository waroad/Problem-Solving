# 해쉬 문제로 여러개의 장르를 받아서 해당 장르에 곡들을 넣고, 그 중 몇 개를 뽑아내서 출력하는 문제이다.
# 구글에서 기본형인 insert, search가 있는 트라이를 가져와서, 조금 수정해 모든 항목을 heapq에 넣어 출력했다.
import heapq
arr=[]


class Node(object):
    def __init__(self,key):
        self.key=key
        self.child={}
        self.count=0


class Trie(object):
    def __init__(self):
        self.head=Node(None)

    def insert(self,word,i,num):
        cur=self.head
        for ch in word:
            if ch not in cur.child:
                cur.child[ch]=Node(ch)
            cur=cur.child[ch]
        if '*' not in cur.child:
            cur.child['*']=[]
        heapq.heappush(cur.child['*'],[num,i])
        cur.count+=num

    def view(self,cur):
        for key in cur.child:
            if key=='*':
                if len(cur.child['*'])>1:
                    heapq.heappush(arr,[cur.count,heapq.heappop(cur.child['*']),heapq.heappop(cur.child['*'])])
                else:
                    heapq.heappush(arr,[cur.count,heapq.heappop(cur.child['*'])])
            else:
                self.view(cur.child[key])


def solution(genres, plays):
    trie = Trie()
    for i in range(len(genres)-1,-1,-1):
        trie.insert(genres[i],i,-1*plays[i])
    trie.view(trie.head)
    answer = []
    while arr:
        tmp = heapq.heappop(arr)
        answer.append(tmp[1][1])
        if len(tmp)>2:
            answer.append(tmp[2][1])
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop", "song"],[500, 600, 500, 800, 2500, 10]))
