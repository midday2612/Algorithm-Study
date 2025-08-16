def solution(arr):
    min_val = sorted(arr)[0]
    arr.remove(min_val)
    if len(arr) == 0:
        return [-1]
    else:
        return arr