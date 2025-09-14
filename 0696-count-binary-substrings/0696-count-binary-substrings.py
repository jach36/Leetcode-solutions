class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0 
        prev = 0
        l, r = 0, len(s)
        while l < r:
            count = 1
            while l < r - 1 and s[l] == s[l + 1]:
                count += 1 
                l += 1
            
            if prev > 0:
                res += min(prev,count)
                
            prev = count 
            l += 1

        return res