def solution(a, b):
    if a ==b:
        return a
    if a>b:
        a, b = b, a
    return (b*(b+1) // 2) - (a*(a-1) // 2)
