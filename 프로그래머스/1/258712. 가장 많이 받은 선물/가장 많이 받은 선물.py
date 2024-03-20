def solution(friends, gifts):
    gift_matrix = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    
    friend_dict={}
    result_dict={}
    gift_dict={}
    for i in range(len(friends)):
        friend_dict[friends[i]] = i
        gift_dict[friends[i]] = 0
        result_dict[i] = 0
    
    
    for i in range(len(gifts)):
        gifts[i] = gifts[i].split(" ")
    
    # 주고받은 선물 표 생성
    for gift in gifts:
        x=friend_dict[gift[0]]
        y=friend_dict[gift[1]]
        gift_matrix[x][y]+=1
        
    
    # 선물 지수
    for i in range(len(gift_matrix)):
        gift_dict[friends[i]] = sum(gift_matrix[i])
        for j in range(len(gift_matrix)):
            gift_dict[friends[i]] -= gift_matrix[j][i]
    
            
    result=[0]*len(friends)
    for i in range(len(gift_matrix)):
        for j in range(len(gift_matrix)):
            if (gift_matrix[i][j] > gift_matrix[j][i]):
                result[i]+=1
            elif (gift_matrix[i][j]==gift_matrix[j][i]) and (i!=j):
                print(i, j)
                if gift_dict[friends[i]] > gift_dict[friends[j]]:
                    result[i]+=1
    
    
    
    return max(result)