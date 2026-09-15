class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we first want to check if the length of both strings are equal
        if len(s) != len(t):
            return False
        
        #initialize empty dictionary to store key values of each character in string S and T
        countS, countT = {}, {}
        #loop through each iteration in length of string s 
        for i in range(len(s)):
            #count each occurence of a character at a specific index i (ex. s[i], value of s at index i)
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        #now compare both countS and countT dictionaries
        for character in s:
            if countS[character] != countT.get(character, 0):
                return False
        
        return True