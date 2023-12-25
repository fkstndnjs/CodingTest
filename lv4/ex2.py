def solution(words, queries):
    trie = {}
    reverse_trie = {}
    length_dict = {}  # 각 길이별 단어의 수를 저장하는 딕셔너리

    def insert(word, trie):
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
            node['count'] = node.get('count', 0) + 1

    def search(query, trie):
        node = trie
        for char in query:
            if char == '?':
                return node.get('count', 0)
            if char not in node:
                return 0
            node = node[char]
        return node.get('count', 0)

    for word in words:
        length = len(word)
        length_dict[length] = length_dict.get(length, 0) + 1  # 길이별 단어 수 갱신
        trie.setdefault(length, {})
        reverse_trie.setdefault(length, {})
        insert(word, trie[length])
        insert(word[::-1], reverse_trie[length])

    answer = []
    for query in queries:
        length = len(query)
        if all(char == '?' for char in query):  # 쿼리의 모든 문자가 와일드카드인 경우
            answer.append(length_dict.get(length, 0))
        elif query[0] == '?':
            answer.append(search(query[::-1], reverse_trie.get(length, {})))
        else:
            answer.append(search(query, trie.get(length, {})))

    return answer
