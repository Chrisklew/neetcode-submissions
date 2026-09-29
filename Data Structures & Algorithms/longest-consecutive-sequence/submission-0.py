class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = sorted(nums)

        current_length = 1
        outcome = 1
        for i in range(1, len(res)):
            curr = res[i]
            prev = res[i-1]
            if curr == prev:
                continue
            if curr - prev == 1:
                current_length += 1
            else:
                current_length = 1
            
            outcome = max(outcome, current_length)
        
        return outcome
