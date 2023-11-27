from collections import deque

def can_transform(word1, word2):
    diff_count = sum([1 for a, b in zip(word1, word2) if a != b])
    return diff_count == 1

def solution(begin, target, words):
    if target not in words:  # target이 words에 없으면 변환 불가능
        return 0

    visited = set()
    queue = deque([(begin, 0)])  # (단어, 변환 횟수)를 저장

    while queue:
        word, count = queue.popleft()

        if word == target:  # target 단어를 찾으면 변환 횟수를 반환
            return count

        for next_word in words:
            if next_word not in visited and can_transform(word, next_word):
                visited.add(next_word)
                queue.append((next_word, count + 1))

    return 0  # target 단어를 찾지 못했으면 0 반환
