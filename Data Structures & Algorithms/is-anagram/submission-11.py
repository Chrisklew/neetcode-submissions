class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in s:
            countS[i] = 1 + countS.get(i, 0)
        
        for j in t:
            countT[j] = 1 + countT.get(j, 0)
        
        print(countS, countT)
        
        for c in s:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
            