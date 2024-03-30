def solution(a, b, c, d):
    num = [a, b, c, d]
    
    dict_num={} # 주사위의 같은 숫자의 갯수를 담을 딕셔너리
    for n in num:
        if n in dict_num:
            dict_num[n]+=1
        else:
            dict_num[n]=1
            
    # 주사위의 같은 숫자의 갯수에 따라 딕셔너리 정렬
    dict_num = sorted(dict_num, key=lambda x: dict_num[x])
    
    if len(dict_num)==1:    # 네 개가 같은 수인 경우
        return (1111*dict_num[0])
    elif len(dict_num)==2:  # [1, 3] 혹은 [2, 2]로 나뉘었을 경우
        if num.count(dict_num[0])==1:
            return (10 * dict_num[1]+dict_num[0])**2
        else:
            return (dict_num[0]+dict_num[1]) * abs(dict_num[0]-dict_num[1])
    elif len(dict_num)==3:  # [1, 1, 2]인 경우
        if num.count(dict_num[2])==2:
            return dict_num[0]*dict_num[1]
        
    
    return min(num)