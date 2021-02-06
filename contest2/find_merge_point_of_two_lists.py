# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def findMergeNode(head1, head2):
    def getCount(head):
        count = 0
        while head.next != None:
            head = head.next
            count += 1
        return count

    def getCommonNode(diff, head1, head2):
        for i in range(diff):
            head1 = head1.next
        while head1 and head2:
            if head1 == head2:
                return head1.data
            else:
                head1 = head1.next
                head2 = head2.next

    count1 = getCount(head1)
    count2 = getCount(head2)
    if count1 > count2:
        return getCommonNode(count1-count2, head1, head2)
    else:
        return getCommonNode(count2 - count1, head2, head1)
