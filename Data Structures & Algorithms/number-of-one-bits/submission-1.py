class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        i = 0
        while i < 32:
            masked_result = (1 << i) & n
            if masked_result != 0:
                bits = bits + 1
            i = i + 1
        return bits
