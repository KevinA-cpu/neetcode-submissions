class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        maxed = (temperatures[0], 0)
        stack = [maxed]
        length = len(temperatures)
        result = [0] * length
        for i in range(1, length):
            lastTemp = stack[-1]
            if temperatures[i] > lastTemp[0]:
                while(stack and stack[-1][0] < temperatures[i]):
                    temperature = stack.pop()
                    result[temperature[1]] = i - temperature[1]
    
            stack.append((temperatures[i], i))
        
        return result