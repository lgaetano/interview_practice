"""
Given the head of a singly linked list, return true if it is a palindrome.
"""

# racecar

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next 
        self.prev = prev

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, value):
        new_node = Node(value, next=self.head)

        if self.head != None:  
            self.head.prev = new_node
            self.head = new_node

        else: # if list is empty
            self.head = new_node
            self.tail = new_node


    def print_ll(self):
        if self.head == None:
            print("The list is empty.")

        current = self.head

        while current:
            print(current.value, end=" -> ")
            current = current.next

    def reverse(self):
        if self.head == None:
            return

        current = self.head
        prev = None
        next = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def is_palindrome(self):
        if self.head == self.tail:
            return False

        current_head = self.head
        current_tail = self.tail

        while current_head != current_tail:
            print(current_head.value)
            print(current_tail.value)
            if current_head.value != current_tail.value:
                return False
            current_head = current_head.next
            current_tail = current_tail.next

        return True



if __name__ == '__main__':
    ll = LinkedList()

    nums = [5, 4, 3, 4, 5]
    for num in nums:
        ll.add_first(num)

    ll.print_ll()
    print()

    print(ll.is_palindrome())
    

    # reversed = ll.reverse()
    # print("Reverse: ", ll.print_ll())
    