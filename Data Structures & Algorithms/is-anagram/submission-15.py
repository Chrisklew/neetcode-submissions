class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #create count of occurence of each character
        counts = collections.defaultdict(int)

        for char in s:
            counts[char] += 1
        
        for char in t:
            counts[char] -= 1
        

        return all(count == 0 for count in counts.values())

