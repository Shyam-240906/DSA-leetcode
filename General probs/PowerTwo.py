"""This leetcode tells about Power of two means if n==2^x , then True"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n &(n-1))==0