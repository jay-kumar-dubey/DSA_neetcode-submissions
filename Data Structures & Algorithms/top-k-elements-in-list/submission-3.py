class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        sort_hash = dict(sorted(hashmap.items(), key = lambda x: x[1], reverse = True)[:k])

        return list(sort_hash.keys())
            









