"""
Given the head of a singly linked list, 
reverse the list, and return the reversed list.

"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):
        self.head = Node(value, self.head)

    def print_list(self):
        if self.head == None:
            print("nothing to print")

        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next

    def reverse(self):
        current = self.head
        prev = None
        next = None

        # 1-2-3-4
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev
        
if __name__ == '__main__':
    ll = LinkedList()

    nums = [1, 2, 3, 4, 5]
    for num in nums:
        ll.add_first(num)

    ll.print_list()

    print()
    ll.reverse()
    ll.print_list()
