class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counterS, counterT = {}, {}
        #example 1
        #r : 2 , a : 2 , c : 2 , e : 1
        for i in range(len(s)):
            counterS[s[i]] = 1 + counterS.get(s[i], 0)
            counterT[t[i]] = 1 + counterT.get(t[i], 0)
        
        for character in s:
            if counterS[character] != counterT.get(character, 0):
                return False
        
        return True
        