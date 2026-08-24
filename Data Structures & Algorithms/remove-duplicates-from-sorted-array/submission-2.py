class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currentp = 1
        nextp = 1

        # while currentp != len(nums) and nextp != len(nums):

        #     if nums[currentp] == nums[nextp]:
        #         nums.pop(nextp)
        #     else:
        #         currentp += 1
        #         nextp += 1

        # return len(nums)

        while currentp != len(nums) and nextp != len(nums):

            if nums[currentp-1] == nums[nextp]:
                nextp += 1
            else:
                nums[currentp] = nums[nextp]
                currentp += 1
                nextp += 1


        return currentp