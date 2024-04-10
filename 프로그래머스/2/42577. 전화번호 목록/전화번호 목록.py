from collections import Counter

def solution(phone_book):
    phone_dict = set(phone_book)
        
    for phone_num in phone_book:
        num=""
        for digit in phone_num:
            num+=digit
            if num in phone_dict and num != phone_num:
                return False
            
    return True