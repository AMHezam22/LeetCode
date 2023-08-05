# https://leetcode.com/problems/binary-search/

def getMid(right, left):
    return (left + right) >> 1


class Solution:
    arr = []

    # it's usually implement recursive binarySearch. but iterative is much faster than recursive in python.
    def binarySearch(self, left, right, target):
        while 1:
            if left > right:
                return left
            mid = getMid(left, right)
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

    def search(self, nums: list[int], target: int) -> int:
        self.arr = nums
        return self.binarySearch(0, len(self.arr) - 1, target)


a = Solution()
print(a.search([1, 3, 5, 6], 0))
