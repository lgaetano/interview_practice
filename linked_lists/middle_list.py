"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are __two middle nodes__, return the __second middle__ node.

"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):
        self.head = Node(value, next=self.head)
    
    def find_middle(self):
        if self.head == None: 
            return None

        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

if __name__ == '__main__':
    ll = LinkedList()

    nums = [5, 4, 3, 2, 1]

    for num in nums:
        ll.add_first(num)

    mid = ll.find_middle()
    print(mid.value)