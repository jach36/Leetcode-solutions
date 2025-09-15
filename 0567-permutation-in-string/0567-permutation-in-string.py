class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l = 0
        count = 0
        comp = 0
        for i in s1:
            comp += ord(i)

        for r in range(len(s2)):
            count += ord(s2[r])

            while(r - l + 1) > len(s1):
                count -= ord(s2[l])
                l += 1

            if count == comp:
                if sorted(s1) == sorted(s2[l:r + 1]):
                    return True
        return False