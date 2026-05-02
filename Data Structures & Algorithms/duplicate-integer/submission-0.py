class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # put array into set
        myset = set(nums)
        # compare length of array with set
        # if the lengths are equal, output false
        if len(myset) == len(nums):
            return False
        # else output true
        else:
            return True