from collections import Counter
class Solution:
    '''
    https://leetcode.com/problems/valid-anagram/
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        # sdict= [i for i in s]
        # scounter = Counter(sdict)
        # tdict=[i for i in t]
        # tcounter = Counter(tdict)
        # if (scounter == tcounter):
        #     return True
        # else:
        #     return False
        scounter= Counter(s)
        tcounter=Counter(t)
        if scounter == tcounter:
            print('True')
            return True
        return False



s1 = Solution()
s1.isAnagram('anagram','nagaram')