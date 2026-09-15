class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        for n in nums:
            #count occurence of number at n
            majority[n] = 1 + majority.get(n, 0)
        
        for number, count in majority.items():
            if count > len(nums) // 2:
                return number
