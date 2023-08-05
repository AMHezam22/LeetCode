# https://leetcode.com/problems/first-bad-version
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right = 1,n
        ans = 0
        while left<=right:
            mid =(left+right)>>1
            if isBadVersion(mid):
                ans = mid
                right=mid-1
            else:
                left = mid+1
        return ans