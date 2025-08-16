def solution(s):
    s_list = list(s)
    print(s_list)
    s_list.sort(reverse = True)
    answer = "".join(s_list)
    return answer