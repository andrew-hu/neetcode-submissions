# Notes: have to filter for alphanumeric string
# O(n) time and O(1) space

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_string = ''.join(filter(str.isalnum, s))
        #print("Filtered string is", alphanumeric_string)
        left = 0
        right = len(alphanumeric_string)-1
        while left < right:
            #print("Left is", alphanumeric_string[left].lower())
            #print("Right is", alphanumeric_string[right].lower())
            if alphanumeric_string[left].lower() != alphanumeric_string[right].lower():
                return False
            else:
                left = left + 1
                right = right - 1
                continue
        return True