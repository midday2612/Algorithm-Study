import heapq

def solution(k, score):
    min_heap = []
    answer = []
    for x in score:
        heapq.heappush(min_heap, x)
        
        if len(min_heap) > k: 
            heapq.heappop(min_heap)
        answer.append(min_heap[0])
        
        
    return answer