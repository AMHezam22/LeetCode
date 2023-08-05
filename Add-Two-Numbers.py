# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def change(self, root):
        text = ''
        temp = root
        while temp:
            text+=str(temp.val)
            temp = temp.next
        return text
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.change(l1)
        num2 = self.change(l2)
        ans = str(int(num1[::-1]) + int(num2[::-1]))
        root = ListNode(int(ans[-1]))
        pointer = root
        for x in range(-2,-len(ans)-1,-1):
            pointer.next = ListNode(ans[x])
            pointer = pointer.next
        return root