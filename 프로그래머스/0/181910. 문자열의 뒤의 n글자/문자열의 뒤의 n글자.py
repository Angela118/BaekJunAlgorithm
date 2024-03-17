def solution(my_string, n):
    answer = ''
    for x in my_string[len(my_string)-n:]:
        answer+=x
    return answer