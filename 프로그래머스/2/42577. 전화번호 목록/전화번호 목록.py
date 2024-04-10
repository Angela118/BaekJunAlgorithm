def solution(phone_book):
        # 문자열 정렬    
        phone_book.sort()    
        
        for i in range(len(phone_book)-1):  # 같은 문자(숫자) 기준으로 정렬 됐기 때문에, 앞 뒤만 비교하면 됨!        
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:            
                return False 
        return True
        