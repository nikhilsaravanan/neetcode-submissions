class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numHash = {} # value, frequency
        for num in nums:
            if num in numHash:
                numHash[num] += 1
            else:
                numHash[num] = 0
        return sorted(numHash, key=numHash.get, reverse = True) [:k]