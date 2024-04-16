def solution(clothes):
    dict_clothes={}
    for i in range(len(clothes)):
        if clothes[i][1] not in dict_clothes:
            dict_clothes[clothes[i][1]]=1
        else:
            dict_clothes[clothes[i][1]]+=1
            
    # if len(dict_clothes)==1:
    #     return len(clothes)
        
    mul=1
    for i in dict_clothes.values():
        mul*=(i+1)

    return mul-1
        