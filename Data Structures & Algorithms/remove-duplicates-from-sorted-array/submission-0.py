class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currentp = 0
        nextp = 1

        while currentp != len(nums) and nextp != len(nums):

            if nums[currentp] == nums[nextp]:
                nums.pop(nextp)
            else:
                currentp += 1
                nextp += 1

        return len(nums)