# 트라이, 골드 2, 40분 정도
# 프로그래머스에서 푼 트라이 코드를 가져와서 조금 수정해서 풀었다. https://programmers.co.kr/learn/courses/30/lessons/42579
# 트라이는 그냥 복붙이 최고인 것 같다. 다시 처음부터 짜기에는 그만큼 익숙하진 않다.
# 이게 트라이로 저장하고, 또 트라이 안에 저장되어 있는 값들을 오름차순으로 출력해야 하는데
# 트라이에 dict 형태로 저장된 상태에서, dict 를 정렬 할 수 있는 방법은 없다.
# 그래서 고민 좀 하다가 dict 를 정렬한 튜플은 만들 수 있어서 그 튜플에는 여전히 다음 노드의
# 주소가 들어 있기에 튜플을 사용해 풀었다.

class Node(object):
    def __init__(self,key):
        self.key=key
        self.child={}


class Trie(object):
    def __init__(self):
        self.head=Node(None)

    def insert(self,word):
        cur=self.head
        for ch in word:
            if ch not in cur.child:
                cur.child[ch]=Node(ch)
            cur=cur.child[ch]

    def view(self,cur,cnt):
        child_by_order = sorted(cur.child.items())
        for key in child_by_order:
            print("--"*cnt,end='')
            print(key[0])
            self.view(key[1],cnt+1)


n=int(input())
trie = Trie()
for i in range(n):
    tmp=[x for x in input().split()]
    trie.insert(tmp[1:])
trie.view(trie.head,0)
