class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = dict()
        for letter in s:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1
        for letter in t:
            if letter in counter:
                if counter[letter] > 0:
                    counter[letter] -= 1
                else:
                    return False
            else:
                return False
        for count in counter.values():
            if count != 0:
                return False
        return True
        