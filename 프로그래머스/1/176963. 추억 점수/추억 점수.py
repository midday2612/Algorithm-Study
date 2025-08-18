def solution(name, yearning, photo):
    answer = []
    
    dict = {n: y for n,y in zip(name, yearning)}
    
    for people_for_photo in photo:
        sum = 0
        for p in people_for_photo:
            sum +=dict.get(p, 0)
        answer.append(sum)
    
    return answer