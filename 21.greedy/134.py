class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        length = len(gas)
        start, car_gas = 0, 0
        
        for index in range(length):
            if gas[index] + car_gas < cost[index]:
                start = index + 1
                car_gas = 0
            else:
                car_gas += gas[index] - cost[index]
        return start