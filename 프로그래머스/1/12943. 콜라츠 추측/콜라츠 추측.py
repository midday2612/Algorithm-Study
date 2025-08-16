def solution(num):
    now = num
    cnt = 0
    while now != 1:
        if cnt == 500:
            return -1
        if now % 2 ==0:
            now = now // 2
            cnt += 1
        else:
            now = now *3 +1
            cnt += 1

    return cnt