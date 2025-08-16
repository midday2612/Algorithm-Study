def solution(phone_number):
    answer = "*"*(len(phone_number) - 4)
    number = phone_number[-4:]
    print(number)
    return answer+number