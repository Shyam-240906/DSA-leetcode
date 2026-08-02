# This the leetcode problem for finding the Palindrome numbers
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 :
            return False

        rev=0
        org=x
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        if org==rev:
            return True