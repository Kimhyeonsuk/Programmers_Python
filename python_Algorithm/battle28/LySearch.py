
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
class Trie:
    def __init__(self, val, depth=0):
        self.child = {}
        self.num = {}
        self.val = val
        self.depth = depth

    def push(self, word):
        node = self
        while len(word) > 0:
            node.num[len(word)] = node.num.get(len(word), 0) + 1
            if word[0] not in node.child:
                node.child[word[0]] = Trie(word[0], node.depth + 1)
            node = node.child[word[0]]
            word = word[1:]


    def search(self, word):
        node = self
        while len(word) > 0:
            if word[0] == '?':
                return node.num.get(len(word), 0)
            if word[0] not in node.child:
                return 0
            node = node.child[word[0]]
            word = word[1:]

    def __repr__(self):
        return 'num: {}; val: {};'.format(str(self.num), self.val)

def solution(words, queries):
    answer = []
    t1 = Trie('')
    t2 = Trie('')
    for word in words:
        t1.push(word)
        t2.push(word[::-1])

    for query in queries:
        if query[0] != '?':
            val = t1.search(query)
        else:
            val = t2.search(query[::-1])
        answer.append(val)
    return answer