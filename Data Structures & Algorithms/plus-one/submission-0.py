class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        answer = []
        for i in range(len(digits)-1, -1, -1):
            total = digits[i] + carry
            if carry > 0:
                carry -= 1  

            temp = None
            if total >= 10:
                carry+=1
                temp = total % 10
            else:
                temp = total
            answer.append(temp)

        if carry > 0:
            answer.append(carry)
        answer.reverse()
        return answer