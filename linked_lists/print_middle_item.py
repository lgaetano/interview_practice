'''
GeeksForGeeks - Print middle item in a Linked List
https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/

Print value associated with middle element in a linked list of odd length 
and print the second value in the case of an evenly long list. 

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def length_list(self):
        cur = self.head
        count = 0

        while cur:
            count += 1
            cur = cur.next

        return count

    def add_front(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def find_middle(self):
        if not self.head:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def print_ll(self):
        cur = self.head
        
        while cur:
            print(cur.data)
            cur = cur.next

if __name__ == '__main__':

    def test_ll(nums):
        ll = LinkedList()

        for num in nums:
            ll.add_front(num)

        # ll.print_ll()
        # print(f"length = {ll.length_list()}")

        return ll.find_middle()

    assert test_ll([3, 2, 1]) == 2
    assert test_ll([4, 3, 2, 1]) == 3
    assert test_ll([0]) == 0
    assert test_ll([]) == None
    assert test_ll([6, 5, 4, 3, 2, 1]) == 4
