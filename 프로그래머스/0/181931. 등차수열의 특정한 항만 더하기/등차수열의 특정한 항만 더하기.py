def solution(a, d, included):
    n = len(included)
    numbers=[]
    for i in range(n):
        if included[i] is True:
            numbers.append(a+(d*i))
    
    return sum(numbers)