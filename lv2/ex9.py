from collections import deque

def solution(s):
    answer = True
    
    stack = deque()
    
    for c in s:
        stack.append(c)
        if len(stack) >= 2 and stack[-2] == '(' and stack[-1] == ')':
            stack.pop()
            stack.pop()
        
    return False if stack else True