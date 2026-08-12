class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        trail = [0] * 26
        actual = [0] * 26
        for i in range(len(s1)):
            trail[ord(s1[i])- ord('a')] += 1
        
        l = 0

        for r in range(len(s2)):

            actual[ord(s2[r]) - ord('a')] += 1
            if r-l + 1 == len(s1):
                if trail == actual:
                    return True
                
                actual[ord(s2[l])-ord('a')] -= 1

                l+=1
        

        return False


