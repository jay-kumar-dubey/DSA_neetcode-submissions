class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i ]
            else:
                hashmap[target-nums[i]] = i