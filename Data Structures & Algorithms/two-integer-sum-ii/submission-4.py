class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                return [1+left, 1+right]
            elif currentSum < target:
                left += 1
            else:
                right -= 1
        return none