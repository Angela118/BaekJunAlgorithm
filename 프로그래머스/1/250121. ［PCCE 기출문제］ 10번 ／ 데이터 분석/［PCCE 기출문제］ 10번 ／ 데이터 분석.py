def solution(data, ext, val_ext, sort_by):
    answer = []
    
    ext_dict={'code':0,
             'date':1,
             'maximum':2,
             'remain':3}
    
    for i in range(len(data)):
        if data[i][ext_dict[ext]] < val_ext:
            answer.append(data[i])
    
    answer.sort(key=lambda x: x[ext_dict[sort_by]])
    
    return answer