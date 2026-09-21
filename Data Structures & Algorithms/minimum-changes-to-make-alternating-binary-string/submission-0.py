class Solution:
    def minOperations(self, s: str) -> int:
        c0 = 0
        c1 = 0
        for i in range(len(s)):
            ch0 = "0" if i%2 == 0 else "1"
            ch1 = "1" if i%2 == 0 else "0"
            if s[i] != ch0:
                c0 +=1
            if s[i] != ch1:
                c1 += 1
        return min(c0,c1)