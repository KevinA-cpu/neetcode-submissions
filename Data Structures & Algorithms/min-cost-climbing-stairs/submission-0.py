class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if cost is None:
            return 0

        memo = {}
        def recMin(i, memo):
            if i >= len(cost):
                return 0
            elif i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(recMin(i+1, memo), recMin(i+2, memo))
            return memo[i]
        recMin(0, memo)
        print(memo)
        return min(memo[0], memo[1])