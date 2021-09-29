from collections import deque

def solution(bridge_length, weight, truck_weights):
    sec = 1
    truck_weights.reverse()
    bridge = deque([truck_weights.pop()])
    bridge_sec = deque([0])
    while bridge_sec:
        sec += 1
        bridge_sec = deque(map(lambda x : x + 1, bridge_sec))
        if bridge_sec[0] == bridge_length:
            bridge.popleft()
            bridge_sec.popleft()
        if truck_weights:
            if sum(bridge) + truck_weights[-1] <= weight:
                bridge.append(truck_weights.pop())
                bridge_sec.append(0)
    
    return sec
