def solution(n, control):
    dict_control={'w':1, 's':-1, 'd':10, 'a':-10}
    for c in control:
        n += dict_control[c]
    return n