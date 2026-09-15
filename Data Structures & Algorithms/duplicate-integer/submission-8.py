class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #initialize empty set to store unique Nums
        uniqueNums = set()
        for n in nums:
            if n in uniqueNums:
                return True
            uniqueNums.add(n)
        return False