"""
Given the head of a linked list, 
remove the nth node from the end of the list and return its head.
"""
# nth = 3
# 1->2->3->4

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, value):
        # Create new node, set it to point to self.head
        new_node = Node(value, next=self.head)
        
        # If self.head already existed (2+ nodes), point head.prev to current
        if self.head != None:
            self.head.prev = new_node
        
        # Move self.head to point to the new first item in list
        self.head = new_node


    def print_list(self):
        if self.head == None:
            print("No list here...")
            return

        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next

    def delete(self, value):
        # point prev.next to next next
        # Node "next" is prev and Node "prev" is next
        # 1->2->3->4

        if self.head == None:
            return

        # Accounts for self.head as a match
        if self.head.value == value:
            self.head = self.head.next
            self.head.prev = None

        # Now start from second node
        current = self.head.next

        while current:
            if current.value == value:
                prev = current.prev 
                prev.next = current.next
                current.next = None
                break
            else:
                current = current.next

    def length(self):
        count = 0 

        if self.head == None:
            return count

        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def delete_nth_node_from_end(self, n):
        length = self.length()

        if n > length:
            return None

        elif n == length:
            self.delete(self.head.value)

        else:
            search_length = length - n

            current = self.head

            for _ in range(search_length):
                current = current.next

            self.delete(current.value)



if __name__ == '__main__':
    ll = LinkedList()

    nums = [1, 2, 3, 4]
    for num in nums:
        ll.add_first(num)

    ll.print_list()

    ll.delete_nth_node_from_end(4)
    print()
    ll.print_list()