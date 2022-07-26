class Solution:

    '''
    https://leetcode.com/problems/two-sum/

    Algorithm:
    nums = [2,7,11,15], target = 9
    1. store list of number in dictionary with index as values
    2. loop through and add number in list after visited to avoid having the same number twice as a sol
    3. return indices
    '''
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map={}

        for i,n in enumerate(nums):
            num2 = target - n
            if num2 in num_map:
                print([num_map[num2], i])
                return [num_map[num2],i]
            num_map[n]=i
        

        
        

s1 = Solution()
s1.twoSum([2,7,11,15], 9)