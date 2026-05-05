class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) <= 1:
            return [strs]

        sortedstr = ["".join(sorted(s)) for s in strs]

        hashmap = {}

        for s in range(len(sortedstr)):
            if sortedstr[s] in hashmap:
                hashmap[sortedstr[s]].append(strs[s])
            else:    
                hashmap[sortedstr[s]] = [strs[s]]
            

        return list(hashmap.values())
        
        