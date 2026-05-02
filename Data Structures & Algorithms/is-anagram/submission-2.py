class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lengths are different, return false
        if len(s) != len(t):
            return False
        # initialize dicts
        s_count = {}
        t_count = {}
        for char in s:
            s_count[char] = 0 
        for char in t:
            t_count[char] = 0
        # load the each angram into dicts (count the occurence of each letter)
        for char in s:
            s_count[char] += 1
        for char in t:
            t_count[char] += 1
        # compare the value of each key to each other - if any of the keys are different
        for char in s:
            if char not in t_count or s_count[char] != t_count[char]:
                return False
        # then return false
        return True