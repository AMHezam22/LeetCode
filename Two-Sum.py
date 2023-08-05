# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        s = dict() # or use set -> s = set()
        i = 0
        while i < len(nums):
            current_element = nums[i]
            n = target - current_element
            if n in s:
                return [i, s[n]]
            else:
                s[current_element] = i  # if you used set -> s.add(current_element)
            i += 1