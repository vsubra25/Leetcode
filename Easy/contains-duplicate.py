class Solution:
    '''
    https://leetcode.com/problems/contains-duplicate
    '''
    def containsDuplicate(self, nums: list[int]) -> bool:
        count = {}

        for x in nums:
            if x not in count.keys():
                count[x] =x
            else:
                print('True')
                return True
        print('False')
        return False

s1 = Solution()
s1.containsDuplicate([1,2,3,3])