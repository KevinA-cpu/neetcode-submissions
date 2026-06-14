import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        i = 0
        j = length-1
        pattern = r"[a-zA-Z0-9]"
        while(i<j):

            while(i < length and not re.match(pattern, s[i])):
                i+=1

            while(j >= 0 and not re.match(pattern, s[j])):
                j-=1
            if i>j:
               break
            
            if  s[i].lower() != s[j].lower():
                print(s[i], s[j])
                return False
            i+=1
            j-=1
        return True