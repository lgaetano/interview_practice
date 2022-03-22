class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):
        self.head = Node(value, next=self.head)

    def print_list(self):
        if self.head == None:
            return

        current = self.head

        while current:
            print(current.value, end=" -> ")
            current = current.next

    def delete(self, value):
        if self.head == None:
            return None
        
        current = self.head
        prev = None

        if self.head.value == value:
            current = current.next
            self.head = current

        while current:
            if current.value == value:
                prev.next = current.next
                current.next = None

            prev = current
            current = current.next

    def reverse(self):
        if self.head == None:
            return None

        current = self.head
        prev = None
        next = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next 

        self.head = prev





if __name__ == '__main__':
    ll = LinkedList()

    nums = [1, 2, 3, 4]
    for num in nums:
        ll.add_first(num)

    ll.print_list()
    print()

    ll.reverse()
    ll.print_list()
    print()

    ll.delete(1)
    ll.print_list()




# class Node: 
#     def __init__(self, value):
#         self.value = value 
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def add_first(self, value):
#         new_node = Node(value)

#         new_node.next = self.head
#         self.head = new_node

#     def get_first(self):
#         if not self.head:
#             return None
#         return self.head.value

#     def length(self):
#         count = 0 

#         cur = self.head
#         while cur:
#             count += 1
#             cur = cur.next
#         return count
        
#     def get_last(self):
#         if self.head == None:
#             return None

#         cur = self.head
#         while cur.next:
#             cur = cur.next
#         return cur.value


#     #  1 <- 2 <- 3 <- 4
#     def reverse(self):
#         if self.head == None:
#             return None

#         cur = self.head
#         prev = None
#         next = None
        
#         while cur:
#             next = cur.next
#             cur.next = prev
#             prev = cur
#             cur = next

#         self.head = prev

#     def print_ll(self):
#         cur = self.head

#         while cur:
#             print(cur.value, end=" ")
#             cur = cur.next

# if __name__ == '__main__':
#     ll = LinkedList()

#     arr = [1, 2, 3, 4]
#     for item in arr:
#         ll.add_first(item)

#     ll.print_ll()
#     ll.reverse()

