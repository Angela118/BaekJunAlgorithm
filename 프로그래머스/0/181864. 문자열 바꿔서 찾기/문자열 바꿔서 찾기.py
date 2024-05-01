def solution(myString, pat):
    pat = pat.replace('A', 'C').replace('B', 'A').replace('C', 'B')
    
    return 1 if pat in myString else 0