class Solution:
    '''
    https://leetcode.com/problems/valid-palindrome/
    Algorithm:
    1. Trim whitespaces, and non alpha numerica char, convert all to lowercase
    2. check if reverse is equal to the string
    '''
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if i.isalnum() == False:
                s=s.replace(i, '')
        s= s.strip().lower()
        print(s)
        print(s[::-1])
        if s[::-1] == s:
           
            return True
        else: 
            return False

s1 = Solution()
s1.isPalindrome("A man, a plan, a canal: Panama")