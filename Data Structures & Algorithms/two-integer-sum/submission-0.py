class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}
        for i, num in enumerate(nums):
            if (target-num) in numHash:
                return [numHash[target-num], i]
            numHash[num] = i
        return