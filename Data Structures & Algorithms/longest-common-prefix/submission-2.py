class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        try:
            char = strs[0][0]
        except:
            return ""

        char = strs[0][0]
        index = 0
        answer = ""
        while(True):
            for string in strs:
                try:
                    if string[index] != char:
                        return answer
                except:
                    return answer
            answer += char
            index+=1
            try:
                char = strs[0][index]
            except:
                return answer

        return answer