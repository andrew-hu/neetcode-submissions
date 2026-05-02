# straightforward approach is to simply iterate through 0 -> n

# every multiple of 2 is 1 bit
# for example
# 0,1,1,2,1,2,2,3,1,2,2,3

# dp[i] = 1 + dp[i - offset]

class Solution:
    def countBits(self, n: int) -> List[int]:
        # create a list n+1 long
        result = [0]
        if n == 0:
            return result
        i = 1
        # offset starts at 1
        offset = 1
        # while loop n+1 times:
        while i <= n:
            # dp[i] = 1 + dp[i - offset]
            #if offset * 2 = i
            if i == (offset * 2):
                #set offset to current number
                offset = i
            result.append(1+result[i-offset])
            i = i + 1
        return result