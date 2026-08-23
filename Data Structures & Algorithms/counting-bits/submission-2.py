class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]   
        answer = [0] *(n+1)
        answer[1] = 1
        for i in range(2, n+1):
            answer[i] = answer[i>>1] + (i&1)
        
        return answer
