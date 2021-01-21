# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        simple_node = ListNode(0)
        l3 = simple_node
        carry = 0
        while l1 or l2:
            x = (l1.val if l1 else 0)
            y = (l2.val if l2 else 0)

            sum1 = x + y + carry
            carry = sum1 // 10
            rem = sum1 % 10

            new_node = ListNode(rem)
            l3.next = new_node
            l3 = l3.next

            if (l1 != None):
                l1 = l1.next
            if (l2 != None):
                l2 = l2.next

        if carry:
            l3.next = ListNode(carry)
        return simple_node.next
