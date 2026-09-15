class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        #iterating through numeric length of string S
        for i in range(len(s)):
            #count each occurence of a alphanumeric value
            #use get incase hashmap has not seen key before
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in s:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True