def solution(ineq, eq, n, m):
    answer = 0
    if n>m:
        if ineq=='>':
            answer=1
    elif n<m:
        if ineq=='<':
            answer=1
    elif n==m:
        if eq=='=':
            answer=1
        
    return answer