# 프로그래머스 | 햄버거 만들기
def solution(ingredient):
    result = 0             # 만든 햄버거 개수
    current_stack = []     # 현재 쌓인 재료를 추적하는 스택

    for i in ingredient:         # 재료 배열을 순회하면서
        current_stack.append(i)  # 현재 재료를 스택에 추가
       
        # 스택의 끝 4개 재료가 [1, 2, 3, 1]인 경우
        if current_stack[-4:] == [1, 2, 3, 1]:
            del current_stack[-4:]  # 스택에서 빵, 야채, 고기, 빵을 제거
            result += 1  # 햄버거 개수 1 증가
   
    # 최종적으로 만들어진 햄버거 개수 반환
    return result