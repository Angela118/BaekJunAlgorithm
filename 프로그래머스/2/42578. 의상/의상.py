def solution(clothes):
    clothes.sort(key=lambda x: x[1])
    print(clothes)
    
    arr=[]
    dict_clothes={}
    # for i in range(len(clothes)):
    #     if clothes[i][1] not in dict_clothes:
    #         arr=[]
    #         dict_clothes[clothes[i][1]]=0
    #         arr.append(clothes[i][0])
    #     else:
    #         arr.append(clothes[i][0])
    #     dict_clothes[clothes[i][1]] = arr
    
    for i in range(len(clothes)):
        if clothes[i][1] not in dict_clothes:
            dict_clothes[clothes[i][1]]=1
        else:
            dict_clothes[clothes[i][1]]+=1
            
    print(dict_clothes)
    if len(dict_clothes)==1:
        return len(clothes)
    
    
    mul=1
    for i in dict_clothes.values():
        mul*=(i+1)

    return mul-1
        