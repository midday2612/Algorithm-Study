def solution(d, budget):
    answer = 0
    d.sort()
    
    now = 0
    for val in d:
        if (now+val)<=budget:
            now +=val
            answer+=1
        else:
            break
    
    return answer