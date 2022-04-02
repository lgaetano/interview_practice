class Node:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def has_cycle(self):
        if self.head == None:
            return False

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    def add_first(self, val):
        # TODO: validation check for val
        self.head = Node(val, next=self.head)

    def add_last(self, val):
        if self.head == None:
            self.head = Node(val, next=self.head)
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = Node(val)

    def length(self):
        count = 0

        if not self.head:
            return count

        current = self.head
        while current:
            count += 1 
            current = current.next

        return count

    def make_cycle(self, val1, val2):
        if self.head == None:
            return
        
        length = ll.length()

        current = self.head
        pointed_to = None
        for _ in range(length):
            if current.val == val1:
                pointed_to = current

            if pointed_to and current.val == val2:
                current.next = pointed_to

            current = current.next

    
    def print_ll(self):
        if self.head == None:
            print("The list is empty")
            
        current = self.head
        
        length = ll.length()

        for _ in range(length):
            print(current.val, end=" -> ")
            current = current.next

        print()


if __name__ == '__main__':
    nums = [3, 2, 0, -4]

    ll = LinkedList()

    for val in nums:
        ll.add_last(val)

    ll.print_ll()

    ll.make_cycle(2, -4)
    ll.print_ll()