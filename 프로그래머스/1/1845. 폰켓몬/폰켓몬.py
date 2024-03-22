def solution(nums):
    take = len(nums)/2
    nums = set(nums)
    
    if take>len(nums):
        return len(nums)
    else:
        return take