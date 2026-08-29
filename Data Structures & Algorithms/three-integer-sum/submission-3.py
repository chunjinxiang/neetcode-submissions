class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        final = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            if nums[i] == nums[i-1] and i > 0:
                continue

            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if sum3 == 0:
                    final.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif sum3 < 0:
                    left += 1
                else:
                    right -= 1

        return final