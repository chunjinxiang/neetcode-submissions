class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            leftrightSum = numbers[left]+numbers[right]

            if leftrightSum == target:
                return [left+1,right+1]
            elif leftrightSum < target:
                left += 1
            elif leftrightSum > target:
                right -= 1