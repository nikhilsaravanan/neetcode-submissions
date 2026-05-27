class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = set()
        for num in nums:
            if num in nums2:
                return True
            nums2.add(num)
        return False