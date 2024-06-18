class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_tank, curr_tank = 0, 0
        starting_station = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            

            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0
        
    
        return starting_station if total_tank >= 0 else -1

# Example Usage
solution = Solution()
print(solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  
print(solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]))  
