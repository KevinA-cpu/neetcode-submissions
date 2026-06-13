class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {}
        temp = n
        while(True):
            total = 0
            while(temp>0):
                digit = temp % 10
                total+=digit ** 2
                temp = temp // 10
            
            if total == 1:
                return True
            
            if total not in visited:
                visited[total] = True
            elif visited[total]:
                return False
            
            temp = total

