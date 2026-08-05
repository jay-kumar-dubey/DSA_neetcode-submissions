class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        bp = prices[0]
        for sp in prices:
           mp = max(mp,sp-bp)
           bp = min(bp,sp)
        return mp
            

        
            
            
            
