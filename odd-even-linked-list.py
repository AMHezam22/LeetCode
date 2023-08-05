# https://leetcode.com/problems/odd-even-linked-list/submissions/855713200/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = odds_tail = ListNode()
        evens = evens_tail = ListNode()
        i = 1
        temp = head
        while temp:
            if i%2==1:
                odd_temp = ListNode(temp.val,None)
                odds_tail.next = odd_temp
                odds_tail = odds_tail.next
            else:
                even_temp = ListNode(temp.val,None)
                evens_tail.next = even_temp
                evens_tail = evens_tail.next
            temp = temp.next
            i+=1
        odds_tail.next = evens.next
        return odds.next