def solution(x):
    answer = False
    x_list = list(map(int, str(x)))
    if x % sum(x_list) ==0:
        answer = True
    return answer