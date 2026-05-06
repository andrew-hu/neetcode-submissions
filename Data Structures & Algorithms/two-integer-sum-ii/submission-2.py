class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        a = 0
        b = len(numbers)-1
        while a < b:
            if numbers[a] + numbers[b] == target:
                result.append(a+1)
                result.append(b+1)
                return result
            elif numbers[a] + numbers[b] > target:
                b = b - 1
            else:
                a = a + 1

