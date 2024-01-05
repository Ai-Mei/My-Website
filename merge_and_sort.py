from flask import Flask, render_template, request, abort
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Connect the two likend lists together.
def connect_linked_lists(list1, list2):
    current = list1
    while current.next is not None:
        current = current.next
    current.next = list2
    return list1  


def sort_linked_list(head):
    if not head or not head.next:
        return head
    tentative = ListNode(0)
    tentative.next = head
    current = head.next
    last_sorted = head
    while current:
        if current.value < last_sorted.value:
            last_sorted.next = current.next
            prev = tentative
            while prev.next and prev.next.value < current.value:
                prev = prev.next
            current.next = prev.next
            prev.next = current
            current = last_sorted.next
        else:
            last_sorted = current
            current = current.next
    return tentative.next


def create_linked_list(values_str):
    if not values_str.strip():
        return None 
    try:
        values = [int(i) for i in values_str.split()]
    except ValueError:
        return "Invalid input. Values must be integers."
    # Additional Constraints:
    if not (0 <= len(values) <= 50) or not all(-100 <= val <= 100 for val in values):
        return "Invalid input. Please make sure the number of entries is between 0 and 50, and values are between -100 and 100."
    head = ListNode(values[0])
    current = head
    for i in values[1:]:
        current.next = ListNode(i)
        current = current.next

    return head


