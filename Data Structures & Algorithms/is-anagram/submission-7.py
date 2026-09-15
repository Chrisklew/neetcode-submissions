class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            # hashmap key value
            #everytime we see same character in anagram increment count of character 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # verify if both strings are anagrams 
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
           
        return True