class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize a dict
        counter = defaultdict(int) 
        # init return array
        results = []
        # each key in the list is a number, value is the counter
        # go through nums, and each cycle increment the counter of the num
        for num in nums:
            counter[num] += 1
        # while k is > 0
        while k > 0:
            # find key with largest value
            max_key = max(counter, key=counter.get)
            results.append(max_key)
            # remove key/value from nums
            del counter[max_key]
            k = k - 1
        return results