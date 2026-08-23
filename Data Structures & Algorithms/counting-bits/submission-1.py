class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]   
        answer = [0]
        for i in range(1, n+1):
            temp = i
            count=0
            while(temp>0):
                remainder = temp % 2
                if remainder == 1:
                    count+=1
                
                temp=temp//2
            answer.append(count)
        
        return answer
