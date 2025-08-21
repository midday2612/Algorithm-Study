def solution(s):
    
    answer = True
    
    open_b = '('
    close_b = ')'
    
    result = 0
    
    for b in s:
        if b == open_b:
            result += 1
        else:
            result -= 1
        if result < 0: 
            return False
    if result == 0:
        return True
    else:
        return False