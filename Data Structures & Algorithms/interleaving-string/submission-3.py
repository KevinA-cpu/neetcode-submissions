class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # number of substring split from s1 and s2 must be the same or difference is 1
        targetLength = len(s3)
        firstLength = len(s1)
        secondLength = len(s2)
        memo = {}

        def rec(i, j, k, memo):
            if str(j)+str(k) in memo: return memo[str(j)+str(k)]
            if i == targetLength: return True
            if firstLength + secondLength > targetLength: return False

            if j != firstLength and s1[j] == s3[i]:
               if (rec(i+1, j+1,k,memo)):
                    memo[str(j)+str(k)] = True
                    return True
            
            if k != secondLength and s2[k] == s3[i]:
               if (rec(i+1, j, k+1, memo)):
                    memo[str(j)+str(k)] = True
                    return True

            memo[str(j)+str(k)] = False
            return False
            

        return rec(0,0,0,memo)

