def solution(n):
    #n-1을 나누어 떨어지게 하는 가장 작은 자연수
    answer = 2
    while (n-1)%answer !=0:
        answer +=1
    return answer