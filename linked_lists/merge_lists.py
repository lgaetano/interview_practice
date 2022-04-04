"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, val):
        self.head = Node(val, next=self.head)

    def print_ll(self):
        if self.head == None:
            print("Empty List.")

        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print()

if __name__ == '__main__':
    def merge_two_lists(list1, list2):
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        current1 = list1.head
        current2 = list2.head
        merge_list_head = None

        # which list to start
        if current1.val < current2.val:
            merge_list_head = current1
            current1 = current1.next
        else:
            merge_list_head = current2
            current2 = current2.next

        merge_current = merge_list_head

        while current1 and current2:
            if current1.val <= current2.val:
                merge_current.next = current1
                current1 = current1.next
            else:
                merge_current.next = current2
                current2 = current2.next    
            merge_current = merge_current.next

        if current1:
            merge_current.next = current1
        elif current2:
            merge_current.next = current2

        return merge_current
                        


    listA = LinkedList()
    listB = LinkedList()

    numsA = [4, 2, 1]
    numsB = [4, 3, 1]

    for num in numsA:
        listA.add_first(num)

    for num in numsB:
        listB.add_first(num)

    listA.print_ll()
    listB.print_ll()

    
    merge_two_lists(listA, listB)
    listA.print_ll()
    listB.print_ll()
    