class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in hash:
                return [hash[complement], i + 1]
            hash[numbers[i]] = i + 1