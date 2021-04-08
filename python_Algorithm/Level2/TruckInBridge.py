def solution(bridge_length, weight, truck_weights):
    answer = 0
    sec=0
    bridge_list=[]
    curBridgeWeight=0
    while truck_weights:
        if bridge_list:
            compelteNum=0
            for idx,truck in enumerate(bridge_list):
                if sec-truck[1]>=bridge_length:
                    curBridgeWeight-=truck[0]
                    compelteNum+=1
            for i in range(compelteNum):
                bridge_list.pop(0)

            if curBridgeWeight+truck_weights[0]<=weight:
                curBridgeWeight+=truck_weights[0]
                bridge_list.append([truck_weights[0],sec])
                truck_weights.pop(0)
            sec+=1
        else:
            curBridgeWeight+=truck_weights[0]
            bridge_list.append([truck_weights[0],sec])
            truck_weights.pop(0)
            sec+=1
    answer=bridge_list[-1][1]+bridge_length+1
    return answer