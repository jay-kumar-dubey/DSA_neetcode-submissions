class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        p = 1
        count = 0
        while count < len(nums):
            for i, n in enumerate(nums):

                if i == count:
                    continue
                else:
                    p *= n
            
            res.append(p)
            count += 1
            p = 1
        
        return res
        
