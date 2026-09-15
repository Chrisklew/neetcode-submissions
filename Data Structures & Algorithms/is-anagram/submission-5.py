class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countsListS = Counter(s)
        countsListT = Counter(t)
        return countsListS == countsListT