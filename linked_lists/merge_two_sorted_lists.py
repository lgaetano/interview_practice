"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by 
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""

class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        count = 0

        if self.head == None:
            return count
        current = self.head
        while current:
            count += 1
            current = current.next

        return count

    def add_last(self, value):
        if self.head == None:
            self.head = Node(value, next=self.head)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(value)

    def add_list_of_items_last(self, nums):
        for num in nums:
            self.add_last(num)

    def print_list(self):
        if self.head == None:
            print("The list is empty.")

        print("in the print func")
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next

def merge_sorted_lls(list1, list2):
    new_ll = LinkedList()
    current_ll1 = list1.head
    current_ll2 = list2.head

    while current_ll1 != None and current_ll2 != None:
        if current_ll1.value <= current_ll2.value:
            new_ll.add_last(current_ll1.value)
            current_ll1 = current_ll1.next
        else:
            new_ll.add_last(current_ll2.value)
            current_ll2 = current_ll2.next

    if current_ll1 == None:
        while current_ll2:
            new_ll.add_last(current_ll2.value)
            current_ll2 = current_ll2.next
    elif current_ll2 == None:
        while current_ll1:
            new_ll.add_last(current_ll1.value)
            current_ll1 = current_ll1.next
    
    return new_ll
    


if __name__ == '__main__':
    # Creates Linked List
    ll = LinkedList()
    ll2 = LinkedList()

    ll.add_list_of_items_last([1, 2, 4])
    ll2.add_list_of_items_last([1, 3, 4])

    # Merge two sorted linked lists
    new_ll = merge_sorted_lls(ll, ll2)
    new_ll.print_list()
