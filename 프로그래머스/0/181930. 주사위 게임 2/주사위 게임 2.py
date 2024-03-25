def solution(a, b, c):
    sum1 = a+b+c
    sum2 = sum1*(a**2+b**2+c**2)
    sum3 = sum2*(a**3+b**3+c**3)
    
    if a==b and b==c:
        return sum3
    elif (a==c and a!=b) or (b==c and a!=b) or (a==b and a!=c):
        return sum2
    elif a!=b and b!=c:
        return sum1
    