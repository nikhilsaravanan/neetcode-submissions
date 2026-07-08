class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1