def divisor(x):
    divisor_num = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            divisor_num.append(i)
            divisor_num.append(x//i)
    divisor_num = list(set(divisor_num))
    return len(divisor_num)

def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        len_divisor = divisor(i)
        if len_divisor <= limit:
            answer+=len_divisor
        else:
            answer+=power
    
    return answer