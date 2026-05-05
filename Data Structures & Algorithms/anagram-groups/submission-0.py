class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a new dict to keep count for all of the strings in strs
        mydict = defaultdict(list)
        for string in strs:
            key = tuple(sorted(string))
            mydict[key].append(string)
        return list(mydict.values())