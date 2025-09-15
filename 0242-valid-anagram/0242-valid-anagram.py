class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        storeS = {}
        storeT = {}
        for i in s:
            if i in storeS:
                storeS[i] += 1
            else:
                storeS[i] = 1
        for i in t:
            if i not in storeS:
                return False
            if i in storeT:
                if storeT[i] < storeS[i]:  
                    storeT[i] += 1
                else:
                    return False
            else:
                storeT[i] = 1
        if len(storeS) != len(storeT):
            return False
        
        for i in storeS:
            if storeS[i] != storeT[i]:
                return False
            
        return True