# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def has_cycle(head):
    back = front = head
    while front != None and front.next != None:
        back = back.next
        front = front.next.next
        if (back == front):
            return True
    return False
