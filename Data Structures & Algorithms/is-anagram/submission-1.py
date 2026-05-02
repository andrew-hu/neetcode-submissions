class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if strings are different lengths, not angram
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        # initialize dicts
        for char in s:
            dict_s[char] = 0
        for char in t:
            dict_t[char] = 0

        # load 's' into a hash table
        # loop length of 's', increment counter of letter
        for char in s:
            dict_s[char] += 1

        # load 't' into hash table
        # loop length of 't', increment counter of letter
        for char in t:
            dict_t[char] += 1

        # loop through 's' , compare with 't'
        for char in s:
            try: 
                dict_t[char]
            except:
                return False
            else:
                if dict_s[char] !=  dict_t[char]:
                    return False
        return True

