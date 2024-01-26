from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge_queue = deque([0]*bridge_length)
    print(bridge_queue)
    truck_weights = deque(truck_weights)
    time=0
    current_weight=0

    while bridge_queue:
        time+=1
        current_weight -= bridge_queue.popleft()    # 1초에 무조건 한 대 씩은 빠지니까 먼저 빼준다

        if truck_weights:
            if current_weight + truck_weights[0] <= weight:     # 현재 무게+이번에 들어올 트럭의 무게 <=최대 무게
                truck = truck_weights.popleft()     # truck 한 대 들어옴
                bridge_queue.append(truck)
                current_weight += truck
            else:
                bridge_queue.append(0)
                
    answer = time
    return answer