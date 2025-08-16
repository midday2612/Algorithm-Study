def solution(s):
    num_len = s.count("0")+s.count("1")+s.count("2")+s.count("3")+s.count("4")+s.count("5")+s.count("6")+s.count("7")+s.count("8")+s.count("9")
    if (len(s) == 4 or len(s) == 6) and num_len == len(s):
        return True
    else:
        return False
        