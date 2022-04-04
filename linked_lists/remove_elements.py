"""
Given the head of a linked list and an integer val, remove all the nodes of 
the linked list that has Node.val == val, and return the new head.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def add_first(self, val):
        self.head = Node(val, next=self.head)

    def print_ll(self):
        if not self.head:
            print("List empty.")

        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print()

    def remove_elements(self, val):
        if not self.head:
            return None

        prev = None
        current = self.head
        while current:
            if current.val == val and prev == None:
                self.head = current.next
            elif current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next




if __name__ == '__main__':
    ll = LinkedList()

    nums = [7, 7, 7, 7]

    for num in nums:
        ll.add_first(num)

    ll.print_ll()
    
    ll.remove_elements(7)
    ll.print_ll()