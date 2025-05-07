class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anadict=defaultdict(list)

        for s in strs:
            sortedword=''.join(sorted(s))
            anadict[sortedword].append(s)
        
        return list(anadict.values())



        