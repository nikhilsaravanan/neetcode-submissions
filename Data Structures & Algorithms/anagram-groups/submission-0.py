class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordHash = defaultdict(list) # sortedword, words
        for word in strs:
            wordHash[''.join(sorted(word))].append(word)
        return list(wordHash.values())