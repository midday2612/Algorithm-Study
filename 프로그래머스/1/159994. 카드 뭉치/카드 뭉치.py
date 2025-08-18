from collections import deque
def solution(cards1, cards2, goal):
    cards1_deque = deque(cards1)
    cards2_deque = deque(cards2)
    
    goal_deque = deque(goal)
    
    for i in range(len(goal)):
        if goal_deque[0] == (cards1_deque[0] if cards1_deque else None):
            goal_deque.popleft()
            cards1_deque.popleft()
        elif goal_deque[0] == (cards2_deque[0] if cards2_deque else None):
            goal_deque.popleft()
            cards2_deque.popleft()
        else:
            return "No"
    
    return "Yes"