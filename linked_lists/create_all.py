class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head == None:
            print("No list")
            return
        
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next

        print()

        
    def get(self, index: int) -> int:
        if self.head == None:
            return
        
        if index >= self.length():
            return -1
        
        current = self.head
        count = 0
        while count < index:
            current = current.next
            count += 1
            
        return current.value

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, next=self.head)
        

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val, next=self.head)
            return
            
        current = self.head
        while current.next:
            current = current.next
            
        current.next = Node(val, next=None) 
        
    def length(self):
        count = 0
        if self.head == None:
            return count
    
        current = self.head
        while current:
            count += 1
            current = current.next
        
        return count

    def addAtIndex(self, index: int, val: int) -> None:
        if self.head == None and index == 0:
            self.head = Node(val, next=self.head)
            return
        elif self.head == None:
            return
        
        count = 0
        current = self.head
        prev = None
        
        while count < index and current:
            count += 1
            prev = current
            current = current.next
            
        if prev == None:
            self.head = Node(val, next=self.head)
        else:
            prev.next = Node(val, next=current)
            
        
    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return
        
        # If self.head is a match
        if index == 0:
            self.head = self.head.next
            return
            
        current = self.head
        prev = None
        count = 0
        
        while count < index and current:
            count += 1
            prev = current
            current = current.next

        if current == None:
            return
        
        prev.next = current.next
        current.next = None


ll = MyLinkedList()
ll.addAtTail(1)
ll.print_ll()
ll.addAtTail(3)
ll.print_ll()
print(ll.get(1))
# ll.print_ll()
# ll.addAtHead(2)
# ll.print_ll()
# ll.addAtHead(7)
# ll.print_ll()
# ll.addAtHead(3)
# ll.print_ll()
# ll.addAtHead(2)
# ll.print_ll()
# ll.addAtHead(5)
# ll.print_ll()
# ll.addAtTail(5)
# print(ll.get(5))
# ll.deleteAtIndex(6)
# ll.print_ll()
# ll.deleteAtIndex(4)

