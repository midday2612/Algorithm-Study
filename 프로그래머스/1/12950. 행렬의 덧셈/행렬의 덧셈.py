def solution(arr1, arr2):
    answer = []
    
    zip_arr = list(zip(arr1, arr2))
    for x, y in zip_arr:
        new_row = [x1+y1 for x1, y1 in zip(x,y)]
        answer.append(new_row)
    
    return answer