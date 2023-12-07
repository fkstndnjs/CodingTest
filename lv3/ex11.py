from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    weak = weak + [w+n for w in weak]  # 원형을 선형으로 변환

    answer = len(dist) + 1  # 최대 친구 수 + 1로 초기화
    for start in range(length):
        for friends in permutations(dist, len(dist)):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer
