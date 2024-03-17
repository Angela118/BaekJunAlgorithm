def solution(num_list):    
    sum_square = sum(num_list)**2
    mul=1
    for num in num_list:
        mul*=num
        
    return int(mul<sum_square)