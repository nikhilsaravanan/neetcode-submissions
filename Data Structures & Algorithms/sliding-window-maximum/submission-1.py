class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        for i in range(k - 1, len(nums)):
            maxn = min(nums)
            for j in range(l, i + 1):
                maxn = max(maxn, nums[j])
            res.append(maxn)
            l += 1
        return res