class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        for string in strs:
            sorted_text = "".join(sorted(string))
            newHash = hash(sorted_text)
            if newHash not in lookup:
                lookup[newHash] = [string]
            else:
                lookup[newHash].append(string)
        
        answer = []
        for key in lookup:
            answer.append(lookup[key])
        return answer