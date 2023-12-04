from itertools import permutations

def is_banned(user_id, banned_id):
    # 두 문자열의 길이가 다르면 일치하지 않음
    if len(user_id) != len(banned_id):
        return False
    for i in range(len(user_id)):
        # 두 문자열의 해당 위치 문자가 다르면 일치하지 않음
        if banned_id[i] != '*' and banned_id[i] != user_id[i]:
            return False
    return True

def solution(user_id, banned_id):
    answer_set = set()
    # 불량 사용자 아이디 목록에 대한 순열을 생성
    for perm in permutations(user_id, len(banned_id)):
        # 순열에 대응되는 불량 사용자 아이디 목록인지 확인
        if all(is_banned(perm[i], banned_id[i]) for i in range(len(banned_id))):
            # 순열을 정렬하여 중복을 방지
            answer_set.add(tuple(sorted(perm)))
    
    return len(answer_set)
