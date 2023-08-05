# https://leetcode.com/problems/climbing-stairs/
# this problem solution can be found as a fibonacci sequence.
# N(steps) :     1   2    3    4   5   6
# F(n):          1   2    3    5   8   13
# and we can notice that F(n) = F(n-1) + F(n-2)
class Solution:
    d = [0, 1, 2]

    def climbStairs(self, n: int) -> int:
        while n < len(self.d):
            self.d.append(self.d[-1] + self.d[-2])
        return self.d[n]
