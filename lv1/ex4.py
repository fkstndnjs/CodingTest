# 프로그래머스 | 성격 유형 검사하기
def solution(survey, choices):
   
    mbti_score = {
        "R" : 0, # 1번 지표, 라이언형
        "T" : 0, # 1번 지표, 튜브형
        "C" : 0, # 2번 지표, 콘형
        "F" : 0, # 2번 지표, 프로도형
        "J" : 0, # 3번 지표, 제이지형
        "M" : 0, # 3번 지표, 무지형
        "A" : 0, # 4번 지표, 어피치형
        "N" : 0  # 4번 지표, 네오형
    }
   
    choice_score = {
        1 : 3, # 매우 비동의
        2 : 2, # 동의
        3 : 1, # 약간 동의
        4 : 0, # 모르겠음
        5 : 1, # 약간 동의
        6 : 2, # 동의
        7 : 3  # 매우 동의
    }
   
    result = ''
   
    #["FC"]을 예로 들겠습니다.
    #성격유형점수 부여시 숫자가 4보다 작으면 왼쪽 type("F")에 점수부여
    #성격유형점수 부여시 숫자가 5보다 크거나 같으면 오른쪽 type("C")에 점수부여
    for type_, choice in zip(survey, choices):
       
        if choice < 4:
            mbti_score[type_[0]] += choice_score[choice]
       
        elif choice >= 5:
            mbti_score[type_[1]] += choice_score[choice]
       
   
    #mbti_score의 key들을 뽑아 ["R","T","C","F","J","M","A","N"] 만들기
    mbti_keys = list(mbti_score.keys())
   
    #예) {'R': 6, 'T': 1, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    #만든 list(mbti_keys())로 0~1 / 2~3 / 4~5 / 6~7  2개씩 끊어서 비교하기
    for left, right in zip(mbti_keys[::2], mbti_keys[1::2]):
       
        # R와 T / C와 F / J와 M / A와 M을 점수비교하여 더 큰 것을 result 추가
        # 점수동일시 왼쪽에 있는 alp을 추가
        if mbti_score[left] >= mbti_score[right]:
            result += left
        else:
            result += right
   
    return result