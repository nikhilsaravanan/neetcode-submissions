class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tempCount = 1
        count = 1
        update = 0
        nums = sorted(nums)
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                tempCount += 1
                update = 0
            elif nums[i] > nums[i-1] + 1 and update == 0:
                count = tempCount
                tempCount = 1
                update += 1
        if tempCount > count:
            count = tempCount
        return count