class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = dict()
        for word in strs:
            sorted_word = str(sorted(word))
            if str(sorted_word) in lookup:
                lookup[sorted_word].append(word)
            else:
                lookup[sorted_word] = [word]
        return list(lookup.values())