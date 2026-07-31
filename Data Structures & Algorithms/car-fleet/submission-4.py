class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        stack = []

        arr = [[p,s] for p,s in zip(position,speed)]
        sorted_arr = sorted(arr)[::-1]
        
        for p,s in sorted_arr:
            stack.append((target - p)/ s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)