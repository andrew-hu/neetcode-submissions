class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize dict
        mydict = defaultdict(list)
        for string in strs:
            # use a sorted tuple as the key to store string in
            key = tuple(sorted(string))
            mydict[key].append(string)
        return list(mydict.values())