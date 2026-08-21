class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):
            lookfor = target - num
            if lookfor in seen:
                return [seen[lookfor], i]
            seen[num] = i