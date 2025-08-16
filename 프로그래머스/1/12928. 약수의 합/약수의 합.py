import math

def solution(n):
    divisor = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor.append(i)
    sum = 0
    for x in divisor:
        sum += x
        if i != n // x:
                sum += n // x
    return sum