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

    def length(self):
        if self.head == None:
            return 0

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next

        return count

    def delete_nth_node_from_end(self, n):
        # 1-2-3-4-5
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

    nums = [1, 2, 3, 4, 5]
    for num in nums:
        ll.add_first(num)

    # ll.print_list()
    print()


    ll.reverse()
    ll.print_list()
    print()

    # ll.delete_nth_node_from_end(5)

    ll.delete(1)
    ll.print_list()


