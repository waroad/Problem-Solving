# 대경권 프로그래밍 대회 2번 문제. 대략 골드 2~4의 난이도인 것 같다. 1시간 좀 넘게 걸렸다.
# 문제는 A와 B로만 이루어진 문자열이 있을 때 이것을 처음부터 읽으며 처음보는 패턴이 나오면 그걸
# Trie 안에 다음 index 로 저장하고 그 직전까지 있었던 패턴을 정답 배열안에 출력하면 되는 문제다.
# 일단 사전순이기 때문에, 보자마자 거의 바로 Trie 라는 것을 알 수 있어서 바로 구글꺼를 가져와서
# 조금 수정한 뒤, Trie 안에 저장하는 것 까지는 나름 빠르게 할 수 있었다. 하지만 이게 마지막
# 문자열 혹은 그 직전 문자열 쪽을 처리해서 배열에 넣는게 어려워 조금 걸렸다.
# 그래도 몇 번 해본 Trie 가 나와서 빠르게 풀 수 있었는데, 역시 프로그래밍을 많이 해봐야 할 것 같다.

cnt=1


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.num=0


class Trie:
    global cnt

    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        global cnt
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string
        current_node.num=cnt
        cnt+=1

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return current_node.num
        else:
            return False


def solution(text):
    trie = Trie()
    ans=[]
    i=0
    trie.insert('A')
    trie.insert('B')
    while i<len(text):
        if i==len(text)-1:
            ans.append(trie.search(text[i:i+ 1]) - 1)
            break
        tmp=i+1
        pre=i
        while True:
            tmp1=trie.search(text[i:tmp])
            if tmp1:
                tmp+=1
                if tmp>len(text):
                    ans.append(trie.search(text[i:tmp - 1]) - 1)
                    i = tmp - 1
                    break
            else:
                trie.insert(text[i:tmp])
                ans.append(trie.search(text[i:tmp-1])-1)
                i=tmp-1
                break
        if i==pre:
            i+=1
    return ans


print(solution("BBAAA"))
"BBAAA"
"ABABAABAB"
