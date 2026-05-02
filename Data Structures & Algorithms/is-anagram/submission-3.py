class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lengths are different, return false
        if len(s) != len(t):
            return False
        # initialize dict
        count = defaultdict(int)

        # load the each angram into dicts (count the occurence of each letter)
        for char in s:
            count[char] += 1
        for char in t:
            count[char] -= 1
        # compare the value of each key to each other - if any of the keys are different
        for char in s:
            if count[char] != 0:
                return False
        # then return false
        return True